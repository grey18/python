import pybithumb


def get_hpr(ticker):
    df = pybithumb.get_ohlcv(ticker)

    df['buy_target'] = df['open'] + (df['open'] * 0.15)
    df['sell_target'] = df['buy_target'] + (df['buy_target'] * 0.15)
    df['forced'] = df['buy_target'] - (df['buy_target'] * 0.15)
    x = 1

    for i in range(3000):
        if df['close'].iloc[i] >= df['buy_target'].iloc[i]:
            for k in range(i,3000):
                if df['close'].iloc[k] >= df['sell_target'].iloc[i]:
                    x = x * 1.15
                    break
                elif df['close'].iloc[k] <= df['forced'].iloc[i]:
                    x = x * 0.9
                    break
        else:
            pass

    return x


tickers = pybithumb.get_tickers()
for ticker in tickers[0:330]:
    x = get_hpr(ticker)
print(float(x))