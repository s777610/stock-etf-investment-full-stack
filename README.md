# Personal Investment App


This Web-App shows some of my investment. I used Flask as framework to build the web and deployed it on AWS. It retrieves data from "IEX" API and scrapes data from some financial site by Beautifulsoup4. It analyzes data and makes interactive charts on the site by using Pandas and Plotly. It allows users to search any security in the US market. All data are stored in SQLite. I use this App very often to check my portfolio. Moreover, I implement multithreading in order to reduce waiting time when calling IEX API. Because of multithreading, the execution will no block if it calls many API requests in the short period of time. (Python, SQL, JS, SCSS, HTML5, AWS, Docker, Multithreading).

## Docker
### Build
`docker run -i -t -p 5000:5000 stock-etf`

### Run
`docker build -t stock-etf .`


## Features:

### This is the landing page
<hr>
<img width="771" alt="Screen Shot 2019-05-03 at 2 16 43 AM" src="https://user-images.githubusercontent.com/35472776/57129144-60c45d80-6d4a-11e9-90b7-5ed5dd89e073.png">

### This is the landing page as well
<hr>
<img width="776" alt="Screen Shot 2019-05-03 at 2 17 02 AM" src="https://user-images.githubusercontent.com/35472776/57129147-628e2100-6d4a-11e9-9dff-c10adbe8924b.png">

### About me
<hr>
<img width="1177" alt="Screen Shot 2019-05-03 at 2 17 28 AM" src="https://user-images.githubusercontent.com/35472776/57129166-733e9700-6d4a-11e9-978c-2f7eca88b875.png">

### The interactive map for world GDP, the interactive chart way created by Python.
<hr>
<img width="990" alt="Screen Shot 2019-05-03 at 2 17 57 AM" src="https://user-images.githubusercontent.com/35472776/57129171-76398780-6d4a-11e9-9342-bef94a54da93.png">

### My investments
<hr>
<img width="1382" alt="Screen Shot 2019-05-03 at 2 19 05 AM" src="https://user-images.githubusercontent.com/35472776/57129179-7c2f6880-6d4a-11e9-85af-72ba007634fa.png">

### The individual stock, and its interactive chart
<hr>
<img width="1143" alt="Screen Shot 2019-05-03 at 2 19 21 AM" src="https://user-images.githubusercontent.com/35472776/57129202-8cdfde80-6d4a-11e9-9585-28c01eeadc58.png">


<hr>
<img width="1105" alt="Screen Shot 2019-05-03 at 2 19 36 AM" src="https://user-images.githubusercontent.com/35472776/57129204-8fdacf00-6d4a-11e9-8688-1e66512e5ea4.png">

<hr>
<img width="1074" alt="Screen Shot 2019-05-03 at 2 19 44 AM" src="https://user-images.githubusercontent.com/35472776/57129210-91a49280-6d4a-11e9-9f02-5d1c935be630.png">

## Architecture 
```
├── Dockerfile
├── Pipfile
├── Pipfile.lock
├── README.md
├── requirements.txt
└── src
    ├── application.py
    ├── common
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-36.pyc
    │   │   ├── candlestick.cpython-36.pyc
    │   │   ├── create_plot.cpython-36.pyc
    │   │   ├── daily_volume.cpython-36.pyc
    │   │   ├── email_sender.cpython-36.pyc
    │   │   ├── moving_average_plot.cpython-36.pyc
    │   │   └── name_scraper.cpython-36.pyc
    │   ├── candlestick.py
    │   ├── daily_volume.py
    │   ├── email_sender.py
    │   ├── moving_average_plot.py
    │   └── name_scraper.py
    ├── hung_resume.pdf
    ├── models
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── plot.cpython-36.pyc
    │   │   └── security.cpython-36.pyc
    │   ├── plot.py
    │   └── security.py
    ├── site.db
    ├── static
    │   ├── css
    │   │   ├── main.css
    │   │   ├── style.comp.css
    │   │   ├── style.concat.css
    │   │   └── style.prefix.css
    │   ├── image
    │   │   ├── home-image.jpg
    │   │   ├── home01.png
    │   │   ├── home02.png
    │   │   ├── home03.png
    │   │   ├── project1.png
    │   │   ├── project10.png
    │   │   ├── project11.png
    │   │   ├── project12.png
    │   │   ├── project13.png
    │   │   ├── project2.png
    │   │   ├── project3.png
    │   │   ├── project4.png
    │   │   ├── project5.png
    │   │   ├── project6.png
    │   │   ├── project7.png
    │   │   ├── project8.png
    │   │   ├── project9.png
    │   │   └── w.png
    │   ├── js
    │   │   ├── main.bundle.js
    │   │   └── main.js
    │   ├── package-lock.json
    │   ├── package.json
    │   ├── sass
    │   │   ├── abstracts
    │   │   │   ├── _mixins.scss
    │   │   │   └── _variables.scss
    │   │   ├── base
    │   │   │   ├── _animations.scss
    │   │   │   ├── _base.scss
    │   │   │   ├── _typography.scss
    │   │   │   └── _utilities.scss
    │   │   ├── components
    │   │   │   ├── _backtotop.scss
    │   │   │   ├── _btn.scss
    │   │   │   ├── _contact.scss
    │   │   │   ├── _emailConfirmation.scss
    │   │   │   ├── _error.scss
    │   │   │   ├── _guide.scss
    │   │   │   ├── _popup.scss
    │   │   │   └── _search.scss
    │   │   ├── layout
    │   │   │   ├── _footer.scss
    │   │   │   ├── _grid.scss
    │   │   │   ├── _header.scss
    │   │   │   └── _navigation.scss
    │   │   ├── main.scss
    │   │   └── pages
    │   │       ├── _about.scss
    │   │       ├── _home.scss
    │   │       ├── _plot.scss
    │   │       ├── _portfolio.scss
    │   │       ├── _project.scss
    │   │       └── _resume.scss
    │   └── webpack.config.js
    └── templates
        ├── 404.html
        ├── about.html
        ├── email_confirmation.html
        ├── home.html
        ├── layout.html
        ├── plot.html
        ├── project.html
        ├── resume.html
        └── securities_list.html
```
