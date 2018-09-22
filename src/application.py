
from flask import Flask, render_template, request
from common.create_plot import create_plot
from models.security import Security
from common.name_scraper import scrape_name
from flask_sqlalchemy import SQLAlchemy


application = Flask(__name__)
application.config['SECRET_KEY'] = 'mysecretkey'

#############################
"""
to create db, go to terminal and activate env,
open python
from application import db
db.create_all() # create site.db file
from application import Security
security_1 = Security(name='Vanguard Dividend Appreciation ETF', ticker='VIG', purchase_price=83.621112)
db.session.add(security_1)
db.session.commit()

Security.query.all()
Security.query.first()
Security.query.filter_by(ticker='VIG').all()
security_1 is a object
security_1.name # 'Vanguard Dividend Appreciation ETF'
"""
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(application)

class Security(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    ticker = db.Column(db.String(20), unique=True, nullable=False)
    purchase_price = db.Column(db.Float, unique=False, nullable=False)

    def __repr__(self):
        return f"Security_name: {self.name}, ticker: {self.ticker}, purchase at: {self.purchase_price}"



@application.route('/plot/<string:ticker>/<string:name>/<string:daily_return>/<string:cum_return>')
def plot_security(name, ticker, daily_return, cum_return):
    name, current_price, name_color, today_status, last_updated, div1, div2, div3 = create_plot(ticker, name)
    return render_template("plot_stock.html",  current_price=current_price, name_color=name_color,
                           company_name=name, ticker=ticker, today_status=today_status,
                           last_updated=last_updated, daily_return=daily_return, cum_return=cum_return,
                           div1=div1, div2=div2, div3=div3)


@application.route('/')
def home():
    return render_template("home.html")


@application.route('/resume')
def resume():
    return render_template("resume.html")

@application.route('/about')
def about():
    return render_template("about.html")


@application.route('/etf/')
def etf():
    securitys = [Security("Vanguard Dividend Appreciation ETF", "VIG", 83.621112),
                 Security("Vanguard 500 Index Fund", "VOO", 249.830589),
                 Security("Vanguard FTSE Pacific ETF", "VPL", 73.861586),
                 Security("Vanguard Total Stock Market ETF", "VTI", 134.610321),
                 Security("Vanguard Value ETF", "VTV", 101.89723),
                 Security("Vanguard Growth ETF", "VUG", 136.481548),
                 Security("Vanguard High Dividend Yield ETF", "VYM", 84.706677)]
    return render_template("eft.html", securitys=securitys)  # pass security object to eft.html


@application.route('/stock/')
def stock():
    securitys = [Security("Amazon Inc.", "AMZN", 1169.959),
                 Security("Mongodb Inc", "MDB", 59.1745)]
    return render_template("stock.html", securitys=securitys)


@application.route("/search", methods=['POST'])
def search():
    if request.method == 'POST':
        try:
            ticker = request.form["ticker"]
            ticker = ticker.upper()
            security_name = scrape_name(ticker)
            name, current_price, name_color, today_status, last_updated, div1, div2, div3 = create_plot(ticker)
            return render_template("search.html", div1=div1, div2=div2, div3=div3,
                           current_price=current_price, name_color=name_color,
                           ticker=ticker, today_status=today_status,
                           last_updated=last_updated, security_name=security_name)
        except:
            return render_template("search.html", text="Could not find the security, please enter a valid ticker.")


if __name__ == "__main__":
    application.run(debug=True, port=4882)
