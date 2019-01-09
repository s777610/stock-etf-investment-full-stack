import os
from flask_mail import Mail
from flask import Flask, render_template, request, send_file, url_for
from flask_sqlalchemy import SQLAlchemy

from models.plot import Plot
from common.name_scraper import scraper


application = Flask(__name__)
application.config['SECRET_KEY'] = 'mysecretkey'
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.url_map.strict_slashes = False
application.config['MAIL_SERVER'] = 'smtp.gmail.com'
application.config['MAIL_PORT'] = 587
application.config['MAIL_USE_TLS'] = True
# application.config['MAIL_PORT'] = 465
# application.config['MAIL_USE_SSL'] = True
application.config['MAIL_USERNAME'] = os.environ['EMAIL_USERNAME']
application.config['MAIL_PASSWORD'] = os.environ['EMAIL_PASSWORD']

db = SQLAlchemy(application)
mail = Mail(application)


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
    security_name = scraper(ticker)  # 'currect name' or ' '
    try:
        plot = Plot(ticker, security_name)
        return render_template("plot.html", plot=plot)
    except:
        return render_template("plot.html", text="Could not find the security, please enter a valid ticker.")


@application.route('/plot/<string:ticker>/<string:name>/<string:daily_return>/<string:cum_return>')
def plot_security(name, ticker, daily_return, cum_return):
    plot = Plot(ticker, name)
    return render_template("plot.html", plot=plot, daily_return=float(daily_return), cum_return=float(cum_return))


@application.route('/email', methods=['POST'])
def send_email():
    from common.email_sender import send
    sender_email = request.form['sender_email']
    sender_subject = request.form['sender_subject']
    message = request.form['message']
    try:
        send(sender_email, sender_subject, message)
        return render_template("email_confirmation.html", text="The email has been sent successfully, ")
    except:
        return render_template("email_confirmation.html", text="Sorry, The email has been sent unsuccessfully, you can try it later...")


@application.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    application.run(debug=True, host='0.0.0.0')
