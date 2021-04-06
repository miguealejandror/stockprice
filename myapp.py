import yfinance as yf
import streamlit as st
from datetime import date, timedelta

today = date.today()
lastmonth = date.today() + timedelta(days=-30)
st.write("""
# Stock Price App
Mostrando el precio de cierre en acciones y el volumen de Tesla
""")

tickerSymbol = 'TSLA'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start= lastmonth, end= today)

st.write("""## Cierre""")
st.line_chart(tickerDf.Close)
st.write("""## Volumen""")
st.line_chart(tickerDf.Volume)

# Reference https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75