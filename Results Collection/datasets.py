#datasets stored in the datafile, use the following to find them
#Below are the price relatives for various standard datasets

#NYSE (Old) New York Stock Exchange Jul. 3, 1962 ~ Dec. 31, 1984 (daily) 5651 x 36
nyse_o = {'dataset': '../Data/nyse-o.csv', 'start':"1962-07-02", 'end':"1985-01-01"}

#SP500 Standard & Poor's 500 Jan. 2, 1998 ~ Jan. 31, 2003 (daily) 1276 x 25
sp500 = {'dataset':'../Data/sp500.csv', 'start':"1998-01-02", 'end':'2003-01-31'}

#DJA Dow Jones Industrial Average (^DJI) Jan. 14, 2001 ~ Jan. 14, 2003 (daily) 507 x 30
dija = {'dataset':'../Data/dija.csv', 'start': '2001-01-14','end':'2003-01-14'}

#MSCI (1) MSCI World Index Apri. 1, 2006 ~ Mar. 31, 2010 (daily) 1043 x 24
msci = {'dataset:':'../Data/msci.csv','start':'2006-04-01','end':'2010-03-31'}

#NYSE (New) New York Stock Exchange Jan. 1, 1985 ~ Jun. 30, 2010 (daily) 6431 x 23
nyse_n = {'dataset':'../Data/nyse-n.csv','start':'185-01-01','end':'2010-06-30'}

#TSE Toronto Stock Exchange Jan. 4, 1994 ~ Dec. 31, 1998 (daily) 1258 x 88
tse = {'datset':'../Data/tse.csv','start':'1994-01-04','end':'1998-12-31'}

#Index used is the S&P500 data, which was pulled from Yahoo Finance
idx_data = '../Data/idx_sp500.csv'
