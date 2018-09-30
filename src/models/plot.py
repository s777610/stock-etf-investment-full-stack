import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
from pandas_datareader import data as dataread
import datetime
import plotly
import plotly.graph_objs as go
from common.moving_average_plot import moving_average_plot
from common.daily_volume import plot_volume
from common.candlestick import candlestick

# name, current_price, name_color, today_status, last_updated, div1, div2, div3 = create_plot(ticker, name)
# return name, current_price, name_color, today_status, last_updated, div1, div2, div3
class Plot(object):
    def __init__(self, ticker, name=None):
        self.ticker = ticker
        self.name = name
        # from 3 months ago to now
        start = datetime.datetime.now() - datetime.timedelta(days=180)
        end = datetime.datetime.now()
        df = dataread.DataReader(self.ticker, data_source='iex', start=start, end=end)

        self.div1 = candlestick(df)
        self.div2 = moving_average_plot(df)
        self.div3 = plot_volume(df)
        self.last_updated = df.index[-1]
        self.current_price = df.iloc[-1]["close"].round(2)
        self.today_status = self.check_status(df.close[-1], df.open[-1])
        self.name_color = self.check_name_color()

    def check_name_color(self):
        if self.today_status == "Increase":
            name_color = "green"
        else:
            name_color = "red"
        return name_color

    @staticmethod
    def check_status(close, open):
        if close > open:
            value = "Increase"
        elif close < open:
            value = "Decrease"
        else:
            value = "Equal"
        return value
