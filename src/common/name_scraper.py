from bs4 import BeautifulSoup
import requests


def scraper(ticker):
    try:
        #https://www.barchart.com/stocks/quotes/vig
        #url = f"https://www.marketwatch.com/investing/stock/{ticker}"
        url = f"https://www.barchart.com/stocks/quotes/{ticker}"
        request = requests.get(url)
        content = request.content
        soup = BeautifulSoup(content, "html.parser")
        # <h1 class="company__name">MongoDB Inc.</h1>
        security_name = soup.find("span", {"class": "symbol"}).text
        return security_name
    except:
        return None


name = scraper("vig")
print(name)