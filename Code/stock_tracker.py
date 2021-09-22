######################
###Import Libraries###
######################

import yfinance as yf
import time


######################
###Define Functions###
######################

def stock_data(stock):
    '''Retrieve Stock data from Yahoo Finance'''
    tickerDf = yf.download(tickers = stock, period='1d', start='2010-1-1', end='2020-1-25')
    return tickerDf


######################
####Create objects####
######################

#define the ticker symbol
tickerSymbol = 'GRMN GWRE HUBS ICE IDXX IFNNY'


#####################
####Run functions####
#####################

def main():

    #Import Data
    stock_df = stock_data(tickerSymbol)
    print(stock_df)


#Run Main script and record runtime
if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
