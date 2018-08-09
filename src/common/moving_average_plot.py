
from bokeh.plotting import figure
from bokeh.embed import components


def moving_average_plot(df):
    df['Close: 7 Day Mean'] = df['Close'].rolling(window=7).mean()
    df['Close: 14 Day Mean'] = df['Close'].rolling(window=14).mean()

    p = figure(width=1000, height=300, x_axis_type="datetime", sizing_mode='scale_width')
    p.title.text = f"Moving Average"

    p.line(df.index, df["Close"], color="red", alpha=0.5, line_width=2, legend="Close")
    p.line(df.index, df["Close: 7 Day Mean"], color="Orange", alpha=0.5, line_width=2, legend="7 Day Mean")
    p.line(df.index, df["Close: 14 Day Mean"], color="blue", alpha=0.5, line_width=2, legend="14 Day Mean")

    p.legend.location = "top_left"
    p.legend.click_policy = "hide"

    script2, div2 = components(p)
    return script2, div2
