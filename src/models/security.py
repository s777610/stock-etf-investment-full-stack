from common.name_scraper import scraper
from application import db
import datetime
from pandas_datareader import data as dataread
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
from concurrent.futures import ThreadPoolExecutor


class Security(db.Model):
    __tablename__ = "security"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    ticker = db.Column(db.String(20), unique=True, nullable=False)
    purchase_price = db.Column(db.Float, unique=False, nullable=False)
    type = db.Column(db.Integer, unique=False,
                    nullable=False)  # ETF 1, Stock 2



    # should add type, in order to match database
    def __init__(self, name, ticker, purchase_price):
        self.name = name
        self.ticker = ticker
        self.purchase_price = purchase_price

    def json(self):
        return {
            'name': self.name,
            'ticker': self.ticker,
            'purchase_price': self.purchase_price
        }

    def get_df(self):
        start = datetime.datetime.now() - datetime.timedelta(days=4)
        end = datetime.datetime.now()
        df = dataread.DataReader(
            self.ticker, data_source='iex', start=start, end=end)
        self.df = df
        self.open = self.df.iloc[-1]["open"].round(2)
        self.close = self.df.iloc[-1]["close"].round(2)
        self.last_updated = self.df.index[-1]
        self.today_status = self.check_status
        self.daily_return = self.get_daily_return
        self.cum_return = self.get_cum_return
        return
        

    @classmethod
    def find_securities(cls, type):
        securities_list = []
        if type == 'stock':
            securities = cls.query.filter_by(type=2).all()  # 2 is stock
        else:
            securities = cls.query.filter_by(type=1).all()  # 1 is etf
        with ThreadPoolExecutor(max_workers=5) as pool:
            for security in securities:
                data = security.json()
                security = Security(**data)
                pool.submit(security.get_df)
                securities_list.append(security)
            return securities_list

    @property
    def check_status(self):
        open = self.df.open[-1]
        close = self.df.close[-1]
        if close > open:
            value = "Increase"
        elif close < open:
            value = "Decrease"
        else:
            value = "Equal"
        return value

    @property
    def get_daily_return(self):
        return self.df['close'].pct_change(1)[-1].round(3)

    @property
    def get_cum_return(self):
        return (((self.df.iloc[-1]['close'] / self.purchase_price) - 1) * 100).round(2)
