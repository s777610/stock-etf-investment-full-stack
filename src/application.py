from flask import Flask, render_template, request, send_file
from models.plot import Plot
from flask_sqlalchemy import SQLAlchemy
from common.name_scraper import scraper
#from common.error.search_error import TickerError


application = Flask(__name__)
application.config['SECRET_KEY'] = 'mysecretkey'
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.url_map.strict_slashes = False
db = SQLAlchemy(application)

@application.route('/')
def home():
    return render_template("home.html")

@application.route('/about')
def about():
    return render_template("about.html")

@application.route('/project')
def project():
    return render_template("project.html")


@application.route('/resume')
def resume():
    return render_template("resume.html")


@application.route("/download")
def download(): 
    # send new file to users, and allow user to download it instead of opening it on browser
    return send_file("Hung_Resume.pdf", attachment_filename="Hung_Resume.pdf", as_attachment=True)


@application.route('/securitieslist/<string:type>')
def securitieslist(type):
    from models.security import Security
    securities_list = Security.find_securities(type)
    return render_template("securities_list.html", securitys=securities_list, type=type)


@application.route("/search", methods=['POST'])
def search():
    ticker = request.form["ticker"].upper()
    security_name = scraper(ticker) # 'currect name' or ' '
    try:
        plot = Plot(ticker, security_name)
        return render_template("plot.html", plot=plot)
    except:
        return render_template("plot.html", text="Could not find the security, please enter a valid ticker.")


@application.route('/plot/<string:ticker>/<string:name>/<string:daily_return>/<string:cum_return>')
def plot_security(name, ticker, daily_return, cum_return):
    plot = Plot(ticker, name)
    return render_template("plot.html", plot=plot, daily_return=float(daily_return), cum_return=float(cum_return))


if __name__ == "__main__":
    application.run(debug=True, port=4882)
