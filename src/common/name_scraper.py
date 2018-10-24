from bs4 import BeautifulSoup
import requests


def scraper(ticker):
    try:
        url = f"https://www.marketwatch.com/investing/stock/{ticker}"
        request = requests.get(url)
        content = request.content
        soup = BeautifulSoup(content, "html.parser")
        # <h1 class="company__name">MongoDB Inc.</h1>
        security_name = soup.find("h1", {"class": "company__name"}).text
        return security_name
    except:
        return None
