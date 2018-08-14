
from flask import Flask, render_template, request
from src.common.create_plot import create_plot
from src.models.security import Security
from src.common.moving_average_plot import moving_average_plot
from src.common.daily_volume import plot_volume

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


@app.route('/plot/<string:ticker>/<string:name>/<string:daily_return>/<string:cum_return>')
def plot_security(name, ticker, daily_return, cum_return):
    company_name, script1, div1, cdn_css, cdn_js, current_price, name_color, today_status, last_updated, script2, div2, script3, div3 = create_plot(ticker, name)
    return render_template("plot_stock.html", script1=script1, div1=div1, cdn_css=cdn_css,
                           cdn_js=cdn_js, current_price=current_price, name_color=name_color,
                           company_name=company_name, ticker=ticker, today_status=today_status,
                           last_updated=last_updated, daily_return=daily_return, cum_return=cum_return,
                           script2=script2, div2=div2, script3=script3, div3=div3)

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/etf/')
def etf():
    securitys = [Security("Vanguard Dividend Appreciation ETF", "VIG", 83.621112),
                 Security("Vanguard 500 Index Fund", "VOO", 249.830589),
                 Security("Vanguard FTSE Pacific ETF", "VPL", 73.861586),
                 Security("Vanguard Total Stock Market ETF", "VTI", 134.610321),
                 Security("Vanguard Value ETF", "VTV", 101.89723),
                 Security("Vanguard Growth ETF", "VUG", 136.481548),
                 Security("Vanguard High Dividend Yield ETF", "VYM", 84.706677)]
    return render_template("eft.html", securitys=securitys)  # pass security object to eft.html


@app.route('/stock/')
def stock():
    securitys = [Security("Amazon Inc.", "AMZN", 1169.959),
                 Security("Mongodb Inc", "MDB", 59.1745)]
    return render_template("stock.html", securitys=securitys)


@app.route("/search", methods=['POST'])
def search():
    if request.method == 'POST':
        try:
            ticker = request.form["ticker"]
            company_name, script1, div1, cdn_css, cdn_js, current_price, name_color, today_status, last_updated, script2, div2, script3, div3 = create_plot(ticker)
            return render_template("search.html", script1=script1, div1=div1, cdn_css=cdn_css,
                           cdn_js=cdn_js, current_price=current_price, name_color=name_color,
                           company_name=company_name, ticker=ticker, today_status=today_status,
                           last_updated=last_updated,
                           script2=script2, div2=div2, script3=script3, div3=div3)
        except:
            return render_template("search.html", text="Please enter a valid ticker.")


if __name__ == "__main__":
    app.run(debug=True, port=4889)

