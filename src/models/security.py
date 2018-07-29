from pandas_datareader import data
import fix_yahoo_finance as yf
import datetime


class Security(object):
    def __init__(self, name, ticker, trade_price, current_price=None, today_status=None, open=None, close=None, last_updated=None):
        self.name = name
        self.ticker = ticker
        self.trade_price = trade_price
        self.current_price = None
        self.today_status = None
        self.open = None
        self.close = None
        self.last_updated = None
        self.daily_return = None
        self.cum_return = None
        yf.pdr_override()
        start = datetime.datetime.now() - datetime.timedelta(days=4)
        end = datetime.datetime.now()

        df = data.get_data_yahoo(self.ticker, start=start, end=end)

        self.open = df.iloc[-1]["Open"].round(2)
        self.close = df.iloc[-1]["Close"].round(2)

        time_string = df.index[-1].strftime('%m/%d/%Y')
        self.last_updated = time_string

        # self.current_price = df.iloc[-1]["Close"]

        # get new columns, Status
        def inc_dec(close, open):
            if close > open:
                value = "Increase"
            elif close < open:
                value = "Decrease"
            else:
                value = "Equal"
            return value

        df["Status"] = [inc_dec(close, open) for close, open in zip(df.Close, df.Open)]
        self.today_status = df.iloc[-1]["Status"]

        # daily return
        self.daily_return = (df['Close'].pct_change(1)[-1]).round(3)
        # cumulative return
        self.cum_return = (((df.iloc[-1]['Close'] / self.trade_price) - 1) * 100).round(2)


