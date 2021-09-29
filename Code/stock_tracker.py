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

def stock_data(stock, start_date, end_date):
    '''Retrieve opening and closing prices from Yahoo Finance'''
    df = yf.download(tickers=stock, period='1d', start=start_date, end=end_date)
    df.reset_index(inplace=True)
    return df[['Date', 'Open']], df[['Date', 'Close']]

def make_calendar(start, end):
    '''Create calendar for Monday open and Friday close prices'''
    df = nyse.schedule(start_date=start, end_date=end)
    df.reset_index(inplace=True)
    df.rename(columns={'index':'Date'}, inplace=True)
    df['Day'] = df['Date'].dt.day_name()
    monday_df = df[(df['Day'] == 'Monday')]
    friday_df = df[(df['Day'] == 'Friday')]
    return monday_df[['Date', 'Day']], friday_df[['Date', 'Day']]

def merge_data(df1, df2):
    '''Merge stock and calendar data'''
    df = pd.merge(df1, df2, how="inner", on='Date')
    return df.drop(columns=['Day'], axis=1)


######################
####Create Objects####
######################

#Define the ticker symbol
tickerSymbol = 'LMT BA NOC GD RTX LDOS BAESY HII CW HEI AXON AVAV'

#How far back to look for data
days = 365

#Create a calendar
nyse = mcal.get_calendar('NYSE')

#Export Files
export_file = r"C:\Users\matty\OneDrive\Work\Lloyd-Lay\Output\stocks.xlsx"


#####################
####Run Functions####
#####################

def main():

    #Import stock
    opening_stock_df, closing_stock_df = stock_data(tickerSymbol, date.today() - timedelta(days), date.today())

    #Flatten the 2-level columns to 1-level
    for df in (opening_stock_df,closing_stock_df):
        df.columns = [f'{j}' if j != '' else f'{i}' for i,j in df.columns]

    #Import calendar
    monday_df, friday_df = make_calendar(date.today() - timedelta(days), date.today())

    #Merge stock and calendar for opening and closing prices
    opening_calendar_df = merge_data(opening_stock_df, monday_df)
    closing_calendar_df = merge_data(closing_stock_df, friday_df)

    #Append closoing dataframe to opening dataframe, then reset index, sort values, transpose, and round the prices to 2 decimals
    final_df = opening_calendar_df.append(closing_calendar_df).set_index('Date').sort_values('Date').transpose().round(2)
    final_df.to_excel(export_file)

#Run Main script and record runtime
if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
