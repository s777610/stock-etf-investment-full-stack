
import plotly
import plotly.graph_objs as go


def plot_volume(df):
    data = [go.Bar(x=df.index, y=df["volume"])]
    layout = go.Layout(title='Daily Trading Volume',
                    yaxis=go.layout.YAxis(automargin=True))
    div3 = plotly.offline.plot({"data": data, "layout": layout},
                            include_plotlyjs=False, output_type='div', link_text="", show_link="False")
    return div3
