import pandas as pd
import streamlit as st
import yfinance as yf

st.title('Simple Stock Price App')

st.header("Simple Stock Price App")
st.write("Shown are the stock **closing price** and ***volume*** of Google.")

tickerSymbol= 'AAPL'

tickerData= yf.Ticker(tickerSymbol)

tickerDf= tickerData.history(period= 'id', start= '2010-5-31', end= '2020-5-31')

st.write("""

##Colsing Price
         """)
st.line_chart(tickerDf.Close)

st.write("""

##Volume Price
         """)

st.line_chart(tickerDf.Volume)


