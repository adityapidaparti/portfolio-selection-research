from pandas_datareader.data import DataReader as web
from datetime import datetime, timedelta
import pandas as pd
import numpy as np

def dataSetup():
    pass

def computePRM(stocks, start, end):
    data = web(stocks, 'yahoo', start, end)
    # # PRM = PRM.dropna()
    # PRM = PRM.as_matrix()
    # PRM = pd.DataFrame(PRM)
    # PRM.columns = stocks
    return data


#Global Variables for sample datasets to run
FORTUNE10 = ['WMT', 'XOM', 'AAPL', 'BRK', 'MCK', 'UNH', 'CVS', 'GM', 'F', 'T']


#datasets stored in the datafile, use the following to find them
dija = '../Data/dija.csv'
msci = '../Data/msci.csv'
nyse_n = '../Data/nyse-n.csv'
nyse_o = '../Data/nyse-o.csv'
sp500 = '../Data/sp500.csv'
tse = '../Data/tse.csv'
