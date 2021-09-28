######################
###Import Libraries###
######################

import yfinance as yf
import pandas_market_calendars as mcal
import time


######################
###Define Functions###
######################

def stock_data(stock):
    '''Retrieve Stock data from Yahoo Finance'''
    tickerDf = yf.download(tickers = stock, period='1d', start='2010-1-1', end='2020-1-25')
    return tickerDf

def make_calendar():
    '''Create calendar for Monday open and Friday close prices'''
    calendar = nyse.schedule(start_date='2012-07-01', end_date='2012-07-10')
    return calendar


######################
####Create objects####
######################

#define the ticker symbol
tickerSymbol = 'MSFT'

# Create a calendar
nyse = mcal.get_calendar('NYSE')


#####################
####Run functions####
#####################

def main():

    #Import Data
    stock_df = stock_data(tickerSymbol)
    print(stock_df)

    calendar_df = make_calendar()
    print(calendar_df)


#Run Main script and record runtime
if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
