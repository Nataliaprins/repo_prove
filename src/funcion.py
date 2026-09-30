def leer datos de yahoo finance (ticket,start):
    """
    Función para leer datos históricos de Yahoo Finance.
    
    Parámetros:
    ticket (str): El símbolo del ticker de la acción.
    start (str): La fecha de inicio en formato 'YYYY-MM-DD'.
    
    Retorna:
    DataFrame: Un DataFrame con los datos históricos de la acción.
    """
    import yfinance as yf
    import pandas as pd
    
    # Descargar los datos históricos
    datos = yf.download(ticket, start=start)
    
    # Retornar el DataFrame con los datos
    return datos


