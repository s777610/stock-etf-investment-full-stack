import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
from pandas_datareader import data as dataread
import datetime
from application import db


class Security(db.Model):
    __tablename__ = "security"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    ticker = db.Column(db.String(20), unique=True, nullable=False)
    purchase_price = db.Column(db.Float, unique=False, nullable=False)
    type = db.Column(db.Integer, unique=False, nullable=False) # ETF 1, Stock 2

    def __init__(self, name, ticker, trade_price): # should add type, in order to match database
        self.name = name
        self.ticker = ticker
        self.trade_price = trade_price
        start = datetime.datetime.now() - datetime.timedelta(days=4)
        end = datetime.datetime.now()
        df = dataread.DataReader(ticker, data_source='iex', start=start, end=end)

        self.open = df.iloc[-1]["open"].round(2)
        self.close = df.iloc[-1]["close"].round(2)
        self.last_updated = df.index[-1]
        self.today_status = self.check_status(df.close[-1], df.open[-1])
        self.daily_return = (df['close'].pct_change(1)[-1]).round(3)
        self.cum_return = (((df.iloc[-1]['close'] / self.trade_price) - 1) * 100).round(2)

    @staticmethod
    def check_status(close, open):
        if close > open:
            value = "Increase"
        elif close < open:
            value = "Decrease"
        else:
            value = "Equal"
        return value
