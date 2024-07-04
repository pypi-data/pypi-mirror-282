import time
import requests
import pandas as pd
import numpy as np

def fetch_json_from_url(sticker, mins):
    url = f'https://api.vietstock.vn/tvnew/history?symbol={sticker}&resolution={mins}&from=1577811600&to={int(time.time())}'
    referer = 'https://stockchart.vietstock.vn/'

    headers = {'Referer': referer, 'Accept': '*/*', 'User-Agent': 'PostmanRuntime/7.37.3', 'Accept-Encoding': 'gzip, deflate, br'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        res = response.json()
        df = pd.DataFrame(res)
        df['Timestamp'] = pd.to_datetime(df['t'], unit='s', utc=True).dt.tz_convert('Etc/GMT-7').dt.strftime('%Y-%m-%d %H:%M')
        df[['Open', 'Low', 'High', 'Close']] = df[['o', 'l', 'h', 'c']] / 1000
        df['Volume'] = df['v'].astype(int)
        return df[['Timestamp', 'Open', 'Low', 'High', 'Close', 'Volume']]
    
    print(f"Failed to fetch data from URL. Status code: {response.status_code}")
    return None

def create_dataset(sticker, mins):
    df = fetch_json_from_url(sticker, mins)
    if df is not None:
        return df
    else:
        raise ValueError("Failed to create dataset")


class EMAIndicator:
    def __init__(self, close: pd.Series, window: int):
        self.close = close
        self.window = window

    def ema_indicator(self):
        ema = self.close.ewm(span=self.window, min_periods=self.window, adjust=False).mean()    
        return ema

class SMAIndicator:
    def __init__(self, close: pd.Series, window: int):
        self.close = close
        self.window = window

    def sma_indicator(self):
        sma = self.close.rolling(window=self.window, min_periods=self.window).mean()      
        return sma

class RSIIndicator:
    def __init__(self, close: pd.Series, window: int = 14):
        self.close = close
        self.window = window

    def rsi(self):
        delta = self.close.diff() 
        gain = delta.where(delta > 0, 0) 
        loss = -delta.where(delta < 0, 0) 
        avg_gain = gain.ewm(com=self.window - 1, min_periods=self.window, adjust=False).mean() 
        avg_loss = loss.ewm(com=self.window - 1, min_periods=self.window, adjust=False).mean() 
        rs = avg_gain / avg_loss.abs() 
        rsi = 100 - (100 / (1 + rs)) 
        rsi[avg_loss == 0] = 100  
        rsi[avg_loss == -avg_gain] = 100  
        return rsi

class MACDIndicator:
    def __init__(self, close: pd.Series, window_slow: int = 26, window_fast: int = 12, window_sign: int = 9):
        self.close = close
        self.window_slow = window_slow
        self.window_fast = window_fast
        self.window_sign = window_sign
        self.ema_slow = EMAIndicator(close, window_slow).ema_indicator()
        self.ema_fast = EMAIndicator(close, window_fast).ema_indicator()
        self.macd_line = self.macd()
        self.macd_signal_line = self.macd_signal()

    def macd(self) -> pd.Series:
        macd_line = self.ema_fast - self.ema_slow
        return macd_line

    def macd_signal(self) -> pd.Series:
        macd_signal_line = self.macd_line.ewm(span=self.window_sign, min_periods=self.window_sign, adjust=False).mean()
        return macd_signal_line

    def macd_diff(self) -> pd.Series:
        macd_diff_line = self.macd_line - self.macd_signal_line
        return macd_diff_line
    
class BollingerBandsIndicator:
    def __init__(self, close: pd.Series, window: int = 20, window_dev: int = 2):
        self.close = close
        self.window = window
        self.window_dev = window_dev
        self.sma = self.bollinger_mavg()
        self.dev = self.bollinger_std()

    def bollinger_mavg(self):
        bollinger_mavg = SMAIndicator(self.close, self.window).sma_indicator()
        return bollinger_mavg
    
    def bollinger_std(self):
        rolling_windows = np.lib.stride_tricks.sliding_window_view(self.close, self.window)
        stds = np.std(rolling_windows, axis=1)
        stds = np.concatenate([np.full(self.window - 1, np.nan), stds])
        return pd.Series(stds, index=self.close.index)

    def bollinger_hband(self):
        bollinger_hband = self.sma + (self.window_dev * self.dev)
        return bollinger_hband

    def bollinger_lband(self):
        bollinger_lband = self.sma - (self.window_dev * self.dev)
        return bollinger_lband
    
class StochasticOscillatorIndicator:
    def __init__(self, high: pd.Series, low: pd.Series, close: pd.Series, window: int = 14, smooth_window: int = 3):
        self.high = high
        self.low = low
        self.close = close
        self.window = window
        self.smooth_window = smooth_window
        self.lowest_low = self.low.rolling(window=self.window).min()
        self.highest_high = self.high.rolling(window=self.window).max()
 
    def stoch(self):
        stoch_k = 100 * (self.close - self.lowest_low) / (self.highest_high - self.lowest_low)
        return stoch_k

    def stoch_signal(self):
        stoch_d = SMAIndicator(self.stoch(), 3).sma_indicator()
        return stoch_d