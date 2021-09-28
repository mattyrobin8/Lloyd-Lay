######################
###Import Libraries###
######################

import yfinance as yf
import pandas as pd
import pandas_market_calendars as mcal
from datetime import date, timedelta
import time


######################
###Define Functions###
######################

def stock_data(stock, begin_date, end_date):
    '''Retrieve opening and closing prices from Yahoo Finance'''
    df = yf.download(tickers = stock, period='1d', start = begin_date, end = end_date)
    df.reset_index(inplace=True)
    return df[['Date', 'Open', 'Close']]

def make_calendar(begin_date, end_date):
    '''Create calendar for Monday open and Friday close prices'''
    df = nyse.schedule(start_date = begin_date, end_date = end_date)
    df.reset_index(inplace=True)
    df.rename(columns = {'index':'Date'}, inplace = True)
    df['Day'] = df['Date'].dt.day_name()
    df = df[(df['Day'] == 'Monday') | (df['Day'] == 'Friday')]
    return df[['Date', 'Day']]

def merge_data(df1, df2):
    '''Merge stock and calendar data'''
    df = pd.merge(df1, df2, how="inner", on='Date')
    return df


######################
####Create objects####
######################

#Define the ticker symbol
tickerSymbol = 'MSFT GOOG'

#How far back to look for data
days = 31

#Create a calendar
nyse = mcal.get_calendar('NYSE')


#####################
####Run functions####
#####################

def main():

    #Import stock
    stock_df = stock_data(tickerSymbol, date.today() - timedelta(days), date.today())
    print(stock_df)

    #Import calendar
    calendar_df = make_calendar(date.today() - timedelta(days), date.today())
    print(calendar_df)

    #Merge stock and calendar
    stock_calendar_df = merge_data(stock_df, calendar_df)
    print(stock_calendar_df)

#Run Main script and record runtime
if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
