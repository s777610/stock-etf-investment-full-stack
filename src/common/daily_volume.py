from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool, ColumnDataSource


def plot_volume(df):
    df["Date_string"] = df.index.strftime("%Y-%m-%d")

    cds = ColumnDataSource(df[["Volume", "Date_string"]])

    p = figure(width=1000, height=300, x_axis_type="datetime", sizing_mode='scale_width')
    p.title.text = "Volume of stock traded each day"

    p.line("Date", "Volume", color="blue", alpha=0.5, line_width=3, source=cds)
    p.circle("Date", "Volume", fill_color="#0b3da0", size=4, hover_fill_color='firebrick', source=cds)

    hover = HoverTool(tooltips=[("Volume", "@Volume"), ("Date", "@Date_string")], mode='vline')
    p.add_tools(hover)

    script3, div3 = components(p)
    return script3, div3

