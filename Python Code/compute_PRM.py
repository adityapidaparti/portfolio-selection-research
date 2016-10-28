from pandas_datareader.data import DataReader as web
from datetime import datetime, timedelta
from pandas import read_csv

STOCKS = ['WMT', 'XOM', 'AAPL', 'BRK', 'MCK', 'UNH', 'CVS', 'GM', 'F', 'T']
		#above is the Fortune 10.

def compute_PRM(num_days):

	# Get price relatives for list of stocks within a date series
	data = web(STOCKS, 'yahoo', datetime.today()-timedelta(days=num_days), datetime.today())
	PRM = data['Close']/data['Open']
	# print (data['Close'])

	#Cleaning data: removing Nan
	PRM = PRM.dropna()
	# print (PRM.shape)
	return PRM.as_matrix()

test = compute_PRM(10000)

def compute_from_csv(file):
	PRM = read_csv(file, sep=',',header=None)
	return PRM.as_matrix()
