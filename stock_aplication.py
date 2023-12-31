import yfinance as yf
import streamlit as st
import pandas as pd

st.write(""" 
# Simple Stock Price App 
Shown are the stock closing price and volume of google!
         
""")

tickerSymbol= 'GOOGL'

tickerData= yf.Tickers(tickerSymbol)

tickerDf= tickerData.history(period='id', start='2010-1-1', end='2020-1-25')

st.line_chart(tickerDf.close)
st.line_chart(tickerDf.volume)
