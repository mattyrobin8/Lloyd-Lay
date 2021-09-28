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
    return df[['Date', 'Open']], df[['Date', 'Close']]

def make_calendar(begin_date, end_date):
    '''Create calendar for Monday open and Friday close prices'''
    df = nyse.schedule(start_date = begin_date, end_date = end_date)
    df.reset_index(inplace=True)
    df.rename(columns = {'index':'Date'}, inplace = True)
    df['Day'] = df['Date'].dt.day_name()
    monday_df = df[(df['Day'] == 'Monday')]
    friday_df = df[(df['Day'] == 'Friday')]
    return monday_df[['Date', 'Day']], friday_df[['Date', 'Day']]

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
    opening_stock_df, closing_stock_df = stock_data(tickerSymbol, date.today() - timedelta(days), date.today())
    print(opening_stock_df)
    print(closing_stock_df)

    #Import calendar
    monday_df, friday_df = make_calendar(date.today() - timedelta(days), date.today())
    print(monday_df)
    print(friday_df)

    #Merge stock and calendar
    opening_calendar_df = merge_data(opening_stock_df, monday_df)
    closing_calendar_df = merge_data(closing_stock_df, friday_df)
    print(opening_calendar_df)
    print(closing_calendar_df)

#Run Main script and record runtime
if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
