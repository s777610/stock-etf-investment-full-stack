import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
from pandas_datareader import data as dataread
import datetime
import plotly
import plotly.graph_objs as go
from common.moving_average_plot import moving_average_plot
from common.daily_volume import plot_volume


def inc_dec(close, open):
    if close > open:
        value = "Increase"
    elif close < open:
        value = "Decrease"
    else:
        value = "Equal"
    return value

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

        trace = go.Candlestick(x=df.index,
                               open=df.open,
                               high=df.high,
                               low=df.low,
                               close=df.close)
        data = [trace]
        layout = go.Layout(title='Candlestick Chart')
        div1 = plotly.offline.plot({"data": data,
                                    "layout": layout},
                                   include_plotlyjs=False,
                                   output_type='div',
                                   link_text="",
                                   show_link="False")

        div2 = moving_average_plot(df)
        div3 = plot_volume(df)
        self.div1 = div1
        self.div2 = div2
        self.div3 = div3

        # create new columns in order to plot
        df["Status"] = [inc_dec(close, open) for close, open in zip(df.close, df.open)]

        last_updated = df.index[-1]
        self.last_updated = last_updated
        current_price = df.iloc[-1]["close"].round(2)
        self.current_price = current_price
        today_status = df.iloc[-1]["Status"]
        self.today_status = today_status
        if self.today_status == "Increase":
            name_color = "green"
        else:
            name_color = "red"
        self.name_color = name_color
    # get new colums, Status
