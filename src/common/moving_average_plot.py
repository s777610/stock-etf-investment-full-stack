
import plotly
import plotly.graph_objs as go


def moving_average_plot(df):
    df['Close: 7 Day Mean'] = df['Close'].rolling(window=7).mean()
    df['Close: 14 Day Mean'] = df['Close'].rolling(window=14).mean()

    trace_high = go.Scatter(
        x=df.index,
        y=df['Close: 7 Day Mean'],
        name="7 Day Mean",
        line=dict(color='#17BECF'),
        opacity=0.8)

    trace_low = go.Scatter(
        x=df.index,
        y=df['Close: 14 Day Mean'],
        name="14 Day Mean",
        line=dict(color='#7F7F7F'),
        opacity=0.8)

    data = [trace_high, trace_low]
    layout = go.Layout(title='Moving Average')
    div2 = plotly.offline.plot({"data": data, "layout": layout}, include_plotlyjs=False, output_type='div', link_text="",
                        show_link="False")

    return div2

