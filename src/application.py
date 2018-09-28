
from flask import Flask, render_template, request
# from common.create_plot import create_plot
from models.security import Security
from models.plot import Plot
from common.name_scraper import scrape_name
from flask_sqlalchemy import SQLAlchemy



application = Flask(__name__)
application.config['SECRET_KEY'] = 'mysecretkey'

#############################

application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(application)

class Security_db(db.Model):
    __tablename__ = "security"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    ticker = db.Column(db.String(20), unique=True, nullable=False)
    purchase_price = db.Column(db.Float, unique=False, nullable=False)
    type = db.Column(db.Integer, unique=False, nullable=False) # ETF 1, Stock 2

    def __repr__(self):
        return f"Security_name: {self.name}, ticker: {self.ticker}, purchase at: {self.purchase_price}"


@application.route('/plot/<string:ticker>/<string:name>/<string:daily_return>/<string:cum_return>')
def plot_security(name, ticker, daily_return, cum_return):
    plot = Plot(ticker, name)
    return render_template("plot_stock.html", plot=plot, daily_return=daily_return, cum_return=cum_return)


@application.route('/')
def home():
    return render_template("home.html")


@application.route('/resume')
def resume():
    return render_template("resume.html")

@application.route('/about')
def about():
    return render_template("about.html")


@application.route('/securitieslist/<string:type>')
def securitieslist(type):
    securities_list = []
    if type == 'stock':
        securities = Security_db.query.filter_by(type=2).all()
    else:
        securities = Security_db.query.filter_by(type=1).all()
    for security in securities:
        securities_list.append(Security(security.name, security.ticker, security.purchase_price))
    return render_template("securities_list.html", securitys=securities_list, type=type)


@application.route("/search", methods=['POST'])
def search():
    if request.method == 'POST':
        try:
            ticker = request.form["ticker"]
            ticker = ticker.upper()
            security_name = scrape_name(ticker)
            plot = Plot(ticker, security_name)
            return render_template("search.html", plot=plot)
        except:
            return render_template("search.html", text="Could not find the security, please enter a valid ticker.")


if __name__ == "__main__":
    application.run(debug=True, port=4882)
