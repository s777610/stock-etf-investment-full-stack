from bs4 import BeautifulSoup
import requests


def scrape_name(ticker):
    url = f"https://www.marketwatch.com/investing/stock/{ticker}"
    print(url)
    request = requests.get(url)
    content = request.content
    # print(content)
    soup = BeautifulSoup(content, "html.parser")
    # <h1 class="company__name">MongoDB Inc.</h1>
    security_name = soup.find("h1", {"class": "company__name"}).text
    return security_name
