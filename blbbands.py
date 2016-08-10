"""

This file creats Bollinger Bands


"""
import matplotlib.pyplot as plt
import pandas as pd


def get_rolling_mean(df,window=20):

    return pd.rolling_mean(df,window=window)

def get_rolling_std(df,window=20):

    return pd.rolling_std(df,window=window)

def bollinger_bands(df,window =20):
    
    r_mean = get_rolling_mean(df,window)
    r_std = get_rolling_std(df,window)

    upper_band = r_mean + 2 * r_std

    lower_band = r_mean - 2 * r_std

    return upper_band,lower_band


def plot_data(df,window =20):
   plt.figure(211)
   ax = df['Adj Close'].plot(title = "Stock Prices",figsize=(8,6),label="Stock Prices")
   r_mean = get_rolling_mean(df['Adj Close'],window=window)
   r_mean.plot(ax = ax,label ="mean")
   upper,lower = bollinger_bands(df['Adj Close'],window=window)
   upper.plot(ax=ax, label ="upper")
   lower.plot(ax=ax, label ="lower")
   plt.legend(loc="upper left")
   
   plt.figure(212)
   
   (df['Volume']/100000000).plot(kind ='bar',figsize=(8,6),use_index= False)
   plt.show()

    