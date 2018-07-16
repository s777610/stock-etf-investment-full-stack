
from flask import Flask, render_template
from create_plot import create_plot
from pandas_datareader import data
import fix_yahoo_finance as yf
import datetime
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components
from bokeh.resources import CDN  # content delivery network

app = Flask(__name__)

@app.route('/plot/MDB')
def plot_mdb():
    # Using yahoo API
    yf.pdr_override()

    # from 3 months ago to now
    start = datetime.datetime.now() - datetime.timedelta(days=365)
    end = datetime.datetime.now()
    df = data.get_data_yahoo("MDB", start=start, end=end)

    # get new colums, Status
    def inc_dec(close, open):
        if close > open:
            value = "Increase"
        elif close < open:
            value = "Decrease"
        else:
            value = "Equal"
        return value

    # create new columns in order to plot
    df["Status"] = [inc_dec(close, open) for close, open in zip(df.Close, df.Open)]
    df["Middle"] = (df.Open + df.Close) / 2
    df["Height"] = abs(df.Close - df.Open)

    p = figure(x_axis_type='datetime', width=1000, height=300, sizing_mode='scale_width')
    p.title.text = "MongoDB Candlestick Chart"
    p.grid.grid_line_alpha = 0.3  # alpha is level of transparent
    hours_12 = 12 * 60 * 60 * 1000  # millisconds

    # 4 parameter, x value of high point, y value of high point, x value of low point, y value of low point
    p.segment(df.index, df.High, df.index, df.Low, color="Black")

    # 4 parameter, x-axis(datetime), y-axis, width(milliseconds in this case), height
    p.rect(df.index[df.Status == "Increase"], df.Middle[df.Status == "Increase"],
           hours_12, df.Height[df.Status == "Increase"], fill_color='#CCFFFF', line_color='black')
    p.rect(df.index[df.Status == "Decrease"], df.Middle[df.Status == "Decrease"],
           hours_12, df.Height[df.Status == "Decrease"], fill_color='#FF3333', line_color='black')

    # the source code of JS and html, which is tuple(len=2)
    # script1 is JS, div1 is html, both type are string
    script1, div1 = components(p)
    cdn_js = CDN.js_files[0]  # js_files is a list of bokeh source code
    cdn_css = CDN.css_files[0]  # css_files is a list of bokeh source code
    return render_template("plot_mongodb.html", script1=script1, div1=div1, cdn_css=cdn_css, cdn_js=cdn_js)  # pass all data to plot_mongodb.html


@app.route('/plot/AMZN')
def plot_AMZN():
    result = create_plot("amazon", "AMZN")
    name = result[0]
    script1 = result[1]
    div1 = result[2]
    cdn_css = result[3]
    cdn_js = result[4]
    current_price = result[5]
    return render_template(f"plot_{name}.html", script1=script1, div1=div1, cdn_css=cdn_css,
                           cdn_js=cdn_js, current_price=current_price)

@app.route('/plot/VIG')
def plot_VIG():
    result = create_plot("VIG_ETF", "VIG")
    name = result[0]
    script1 = result[1]
    div1 = result[2]
    cdn_css = result[3]
    cdn_js = result[4]
    current_price = result[5]
    return render_template(f"plot_{name}.html", script1=script1, div1=div1, cdn_css=cdn_css,
                           cdn_js=cdn_js, current_price=current_price)

@app.route('/plot/VOO')
def plot_VOO():
    result = create_plot("VOO_ETF", "VOO")
    name = result[0]
    script1 = result[1]
    div1 = result[2]
    cdn_css = result[3]
    cdn_js = result[4]
    current_price = result[5]
    return render_template(f"plot_{name}.html", script1=script1, div1=div1, cdn_css=cdn_css,
                           cdn_js=cdn_js, current_price=current_price)



@app.route('/')
def home():
    return render_template("home.html")

@app.route('/etf/')
def etf():
    return render_template("eft.html")


if __name__ == "__main__":
    app.run(debug=True, port=4888)

