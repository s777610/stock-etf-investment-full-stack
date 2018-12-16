
import datetime
from bs4 import BeautifulSoup
import requests
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
from common.moving_average_plot import moving_average_plot
from common.daily_volume import plot_volume
from common.candlestick import candlestick
from pandas_datareader import data as dataread





class Plot(object):
    def __init__(self, ticker, name):
        self.ticker = ticker
        self.name = name
        self.df = self.get_df()
        self.div1 = candlestick(self.df)
        self.div2 = moving_average_plot(self.df)
        self.div3 = plot_volume(self.df)
        self.last_updated = self.df.index[-1]
        self.current_price = self.get_current_price
        self.today_status = self.check_status

    # from 3 months ago to now

    def get_df(self):
        start = datetime.datetime.now() - datetime.timedelta(days=180)
        end = datetime.datetime.now()
        df = dataread.DataReader(
            self.ticker, data_source='iex', start=start, end=end)
        return df

    @property
    def get_current_price(self):
        return self.df.iloc[-1]["close"].round(2)

    @property
    def check_status(self):
        close = self.df.close[-1]
        open = self.df.open[-1]
        if close > open:
            value = "Increase"
        elif close < open:
            value = "Decrease"
        else:
            value = "Equal"
        return value
