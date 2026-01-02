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
    buyingSent = pyqtSignal(str)

    def __init__(self, tickers):
        super().__init__()
        self.tickers = tickers
        self.alive = True

    def run(self):
        get_target_price(tickers)
        get_yesterday_ma5(tickers)
        wait_flag = False
        while self.alive:
            try:
                for ticker in self.tickers:
                    if wait_flag == False:
                        current_price = pybithumb.get_current_price(ticker) # 추후에 웹소켓 기술 사용할 수 있지 않을까?
                        if (current_price > self.target_price) and (current_price > self.ma5):
                            self.buyingSent.emit(ticker)
                            wait_flag = True
                        time.sleep(0.1)
            except:
                pass

    def close(self):
        self.alive = False


#변동성 돌파 전략 목표가 구하는 함수(단발성)
def get_target_price(tickers):
    for ticker in tickers:
        df = pybithumb.get_ohlcv(ticker)
        yesterday = df.iloc[-2]

        today_open = yesterday['close']
        yesterday_high = yesterday['high']
        yesterday_low = yesterday['low']
        target = today_open + (yesterday_high - yesterday_low) * 0.5
        target_price[ticker] = target # target_price dict에 목표가 저장
    return None

#5일 이동평균 구하는 함수(단발성)
def get_yesterday_ma5(tickers):
    for ticker in tickers:
        df = pybithumb.get_ohlcv(ticker)
        close = df['close']
        ma = close.rolling(5).mean()
        ma5[ticker] = ma #ma5 dict에 평균값 저장
    return None

#암호화폐 매수 함수(단발성) **************추후에 매수 방법 수정 필요*************
def buy_crypto_currency(ticker):
    krw = bithumb.get_balance(ticker)[2]
    orderbook = pybithumb.get_orderbook(ticker)
    sell_price = orderbook['asks'][0]['price']
    unit = krw / float(sell_price)
    bithumb.buy_market_order(ticker, unit)

#암호화폐 매도 함수(단발성) ***************추후에 매도 방법 수정 필요***************
def sell_crypto_currency(ticker):
    unit = bithumb.get_balance(ticker)[0]
    bithumb.sell_market_order(ticker, unit)

tickers = pybithumb.get_tickers() #티커 목록 가져오기
target_price = {}
ma5 = {}

now = datetime.datetime.now()
mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)

pc = PriceComparison(tickers)
pc.buyingSent.connect(buy_crypto_currency)
pc.start()


while True:
    try:
        now = datetime.datetime.now()
        if mid < now < mid + datetime.delta(seconds=10): #자정이 됐을 때
            pc.close()
            mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
            for ticker in tickers:
                sell_crypto_currency(ticker)
            target_price.clear()
            ma5.clear()
            time.sleep(60)
            pc.start()

    except:
        print("에러 발생")
    time.sleep(1)