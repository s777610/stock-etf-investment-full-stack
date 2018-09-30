import plotly
import plotly.graph_objs as go


def candlestick(df):
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
    return div1
