import yfinance as yf
import pandas as pd

def descargar_datos_yf(ticker: str, fecha_inicio: str, fecha_fin: str) -> pd.DataFrame:

    df = yf.download(ticker, start=fecha_inicio, end=fecha_fin, progress=False)

    if df.empty:
        raise ValueError(f"No se encontraron datos para {ticker} entre {fecha_inicio} y {fecha_fin}")

    return df

