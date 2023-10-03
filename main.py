import pandas as pd
import numpy as np
import yfinance as yf

help(yf)

help(yf.Ticker)

df = pd.read_csv('data/IBOVDia_02-10-23.csv', sep=";",
                 encoding_errors='ignore', encoding='latin-1', skiprows=1, skipfooter=2)

acoes = df.iloc[:, 0]
acoes.index = acoes.index + '.SA'

ticks = " ".join(acoes.index)

resp = yf.Tickers(ticks)

new_df = resp.history()
aux = new_df['Close'].reset_index()

aux['Date'] = aux['Date'].astype('str')


with pd.ExcelWriter("data/cotacoes.xlsx", date_format='DD/MM/YYYY') as writer:
    aux.to_excel(writer, index=False)
