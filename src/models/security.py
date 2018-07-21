from pandas_datareader import data
import fix_yahoo_finance as yf
import datetime


class Security(object):
    def __init__(self, name, ticker, current_price=None, today_status=None):
        self.name = name
        self.ticker = ticker
        self.current_price = None
        self.today_status = None

    def get_info(self):
        yf.pdr_override()
        start = datetime.datetime.now() - datetime.timedelta(days=4)
        end = datetime.datetime.now()

        df = data.get_data_yahoo(self.ticker, start=start, end=end)

        self.current_price = df.iloc[-1]["Close"]


        # get new colums, Status
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
        return self.name, self.ticker, self.current_price, self.today_status


# mdb = Security("mongodb", "mdb")
# print(mdb.get_info())
