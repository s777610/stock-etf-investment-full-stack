
from flask import Flask, render_template
from create_plot import create_plot
from src.models.security import Security

app = Flask(__name__)


@app.route('/plot/<string:ticker>/<string:name>')
def plot_security(name, ticker):
    company_name, script1, div1, cdn_css, cdn_js, current_price, name_color, today_status, last_updated = create_plot(name, ticker)
    return render_template("plot_stock.html", script1=script1, div1=div1, cdn_css=cdn_css,
                           cdn_js=cdn_js, current_price=current_price, name_color=name_color,
                           company_name=company_name, ticker=ticker, today_status=today_status,
                           last_updated=last_updated)

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/etf/')
def etf():
    #securitys = Security.get_etfs()
    securitys = [Security("Vanguard Dividend Appreciation ETF", "VIG"),
                 Security("Vanguard 500 Index Fund", "VOO"),
                 Security("Vanguard FTSE Pacific ETF", "VPL"),
                 Security("Vanguard Total Stock Market ETF", "VTI"),
                 Security("Vanguard Value ETF", "VTV"),
                 Security("Vanguard Growth ETF", "VUG"),
                 Security("Vanguard High Dividend Yield ETF", "VYM")]
    return render_template("eft.html", securitys=securitys)


@app.route('/stock/')
def stock():
    securitys = [Security("Amazon Inc.", "AMZN"), Security("Mongodb Inc", "MDB")]
    return render_template("stock.html", securitys=securitys)


if __name__ == "__main__":
    app.run(debug=True, port=4884)

