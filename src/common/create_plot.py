
from pandas_datareader import data as dataread
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import datetime
import plotly
import plotly.graph_objs as go
import fix_yahoo_finance as yf
from src.common.moving_average_plot import moving_average_plot
from src.common.daily_volume import plot_volume


# get new colums, Status
def inc_dec(close, open):
    if close > open:
        value = "Increase"
    elif close < open:
        value = "Decrease"
    else:
        value = "Equal"
    return value


def create_plot(ticker, name=None):
    # Using yahoo API
    yf.pdr_override()

    # from 3 months ago to now
    start = datetime.datetime.now() - datetime.timedelta(days=180)
    end = datetime.datetime.now()

    df = dataread.get_data_yahoo(ticker, start=start, end=end)

    trace = go.Candlestick(x=df.index,
                           open=df.Open,
                           high=df.High,
                           low=df.Low,
                           close=df.Close)
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

    # create new columns in order to plot
    df["Status"] = [inc_dec(close, open) for close, open in zip(df.Close, df.Open)]
    df["Middle"] = (df.Open + df.Close) / 2
    df["Height"] = abs(df.Close - df.Open)

    time_string = df.index[-1].strftime('%m/%d/%Y')
    last_updated = time_string
    current_price = df.iloc[-1]["Close"].round(2)

    today_status = df.iloc[-1]["Status"]
    if today_status == "Increase":
        name_color = "green"
    else:
        name_color = "red"

    return name, current_price, name_color, today_status, last_updated, div1, div2, div3

