import time
import pybithumb
import datetime
from PyQt5.QtCore import QThread, pyqtSignal

#API 키값
with open("bithumb.txt") as f:
    lines = f.readlines()
    key = lines[0].strip()
    secret = lines[1].strip()
    bithumb = pybithumb.Bithumb(key, secret)

#가격 비교 스레드 클래스
class PriceComparison(QThread):
    buyingSent = pyqtSignal(str, int)

    def __init__(self, tickers):
        super().__init__()
        self.tickers = tickers
        self.alive = True

    def run(self):
        while self.alive:
            try:
                now = datetime.datetime.now()
                if later < now < later + datetime.timedelta(seconds=10):
                    later = now + datetime.timedelta(minutes=1)
                    try:
                        for ticker in self.tickers:
                            current_price = pybithumb.get_current_price(ticker)
                            if (current_price > past_price[ticker]):
                                self.buyingSent.emit(ticker, current_price)
                            past_price[ticker] = round(current_price + (current_price * 0.15), 4)
                    except:
                        pass
                time.sleep(1)
            except:
                pass

    def close(self):
        self.alive = False


#매수하기
def buy_crypto_currnecy(ticker, buy_price):
    krw = 20000
    orderbook = pybithumb.get_orderbook(ticker)
    sell_price = orderbook['asks'][0]['price']
    unit = krw / float(sell_price)
    bithumb.buy_market_order((ticker, unit))
    sell_crypto_limit(ticker, buy_price)
    priceInquiry(ticker, buy_price)
    pc.close()
    return None

#시장가 매도하기
def sell_crypto_currency(ticker):
    unit = bithumb.get_balance(ticker)[0]
    bithumb.sell_market_order(ticker, unit)
    pc.start()
    return None

#지정가 매도하기 계속 만들기 반올림 하고 있었음
#50만원 이상은 500, 10만원 이상은 100, 만원은 10, 5천원은 5, 100원은 1, 10원은 0.01, 1원은 0.001, 0원은 0.0001
def sell_crypto_limit(ticker, buy_price):
    sell_price = round(buy_price + buy_price * 0.15, 4)
    if sell_price > 1000000:
        sell_price = round(sell_price, -3)
    elif sell_price > 500000:
        sell_price = round(sell_price, )

def priceInquiry(ticker, buy_price):
    alive = True
    target_price = buy_price + (buy_price * 0.15)
    forced = buy_price - (buy_price * 0.15)

#여기 조건문 잘 수정해서 올바른 조건에서 올바르게 거래 수행되도록 수정필요!!!
    while alive:
        try:
            price = pybithumb.get_current_price(ticker)
            if forced > price:
                sell_crypto_currency(ticker)
                alive = False
            time.sleep(1)
        except:
            pass


tickers = pybithumb.get_tickers() #티커 목록 가져오기

now = datetime.datetime.now()
later = now + datetime.timedelta(minutes=1)
past_price = {}
#past_price 딕셔너리 초기화
for ticker in tickers:
    past_price[ticker] = 999999999

pc = PriceComparison(tickers)
pc.buyingSent.connect(buy_crypto_currnecy)
pc.start()