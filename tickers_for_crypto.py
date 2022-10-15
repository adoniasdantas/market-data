import yfinance as yf

tickers = ['BTC-USD', 'ETH-USD', 'MATIC-USD', 'SOL-USD', 'LTC-USD',
           'AVAX-USD', 'XRP-USD', 'ADA-USD', 'FTM-USD', 'THETA-USD']
columns = ['Date', 'High', 'Low', 'Close']


for ticker in tickers:
    data = yf.download(ticker, interval='1d',
                       period='max', group_by='Ticker')
    currency_data = data.sort_index(ascending=False)
    currency_data = currency_data.reset_index()
    currency_data.Date = currency_data.Date.dt.strftime('%Y-%m-%d')
    file_name = '{0}.xlsx'.format(ticker)
    currency_data.to_excel(file_name, columns=columns, index=False)
