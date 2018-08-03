from pandas_datareader import data
import fix_yahoo_finance as yf
import datetime
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components
from bokeh.resources import CDN  # content delivery network


def moving_average_plot(name, ticker):
    # Using yahoo API
    yf.pdr_override()

    # from 3 months ago to now
    start = datetime.datetime.now() - datetime.timedelta(days=6*30)
    end = datetime.datetime.now()

    df = data.get_data_yahoo("AMZN", start=start, end=end)

    df['Close: 7 Day Mean'] = df['Close'].rolling(window=7).mean()
    df['Close: 14 Day Mean'] = df['Close'].rolling(window=14).mean()

    p = figure(width=500, height=250, x_axis_type="datetime", sizing_mode='scale_width')
    p.title.text="Moving Average"

    p.line(df.index, df["Close"], color="red", alpha=0.5, line_width=2, legend="Close")
    p.line(df.index, df["Close: 7 Day Mean"], color="Orange", alpha=0.5, line_width=2, legend="7 Day Mean")
    p.line(df.index, df["Close: 14 Day Mean"], color="blue", alpha=0.5, line_width=2, legend="14 Day Mean")

    p.legend.location = "top_left"
    p.legend.click_policy="hide"

    script1, div1 = components(p)
    cdn_js = CDN.js_files[0]  # js_files is a list of bokeh source code
    cdn_css = CDN.css_files[0]  # css_files is a list of bokeh source code
    return script1, div1, cdn_css, cdn_js
