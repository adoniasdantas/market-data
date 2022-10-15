import yfinance as yf

tickers = ['MGLU3.SA', 'PETR4.SA', 'USIM5.SA', 'PRIO3.SA', 'CSNA3.SA']
columns = ['Date', 'High', 'Low', 'Close']


for ticker in tickers:
    data = yf.download(ticker, interval='1d', period='max', group_by='Ticker')
    company_data = data.sort_index(ascending=False)
    company_data = company_data.reset_index()
    company_data.Date = company_data.Date.dt.strftime('%Y-%m-%d')
    file_name = '{0}.xlsx'.format(ticker)
    company_data.to_excel(file_name, columns=columns, index=False)
