import pandas as pd
import yfinance as yf
import streamlit as st
import datetime

st.header('Stock Market Analysis', divider='rainbow')


# text input
ticker_symbol = st.text_input("Enter stock symbol", "MSFT", key='placeholder')
ticker_data= yf.Ticker(ticker_symbol)

# layout change adjacent date
col1, col2= st.columns(2)

with col1:
   start_date = st.date_input("Input the start date", datetime.date(2019, 1, 1))

with col2:
    end_date = st.date_input("Input the end date", datetime.date(2024, 5, 31))

#date input and output
#start_date = st.date_input("Input the start date", datetime.date(2019, 1, 1))

# once all data has come with history then plotting will be done, day format 1 day 1d one month "1mo"
ticker_df = ticker_data.history(period ="1d", start=start_date, end=end_date)

st.dataframe(ticker_df)

#chart for close points
st.write("Daily Closing Price Chart")
st.line_chart(ticker_df['Close'])

# chart for volume
st.write("Daily traded volume Chart")
st.line_chart(ticker_df['Volume'])