def leer_datos_de_yahoo_financ (ticket,start):
    import yfinance as yf
    ticket = "NVTS"
    start = "2020-01-01"
    data = yf.download(ticket, start=start)
    return data
