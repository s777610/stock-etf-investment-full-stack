# Personal Investment App


This Web-App shows some of my investment. I used Flask as framework to build the web and deployed it on AWS. It retrieves data from "IEX" API and scrapes data from some financial site by Beautifulsoup4. It analyzes data and makes interactive charts on the site by using Pandas and Plotly. It allows users to search any security in the US market. All data are stored in SQLite. I use this App very often to check my portfolio. Moreover, I implement multithreading in order to reduce waiting time when calling IEX API. Because of multithreading, the execution will no block if it calls many API requests in the short period of time. (Python, SQL, JS, SCSS, HTML5, AWS, Docker, Multithreading).

## Docker
### Build
`docker run -i -t -p 5000:5000 stock-etf`

### Run
`docker build -t stock-etf .`
