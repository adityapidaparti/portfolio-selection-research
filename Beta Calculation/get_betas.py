from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import os.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from datasets import *

def getBetas(data=nyse_o, beta_range = 180, idx_data=idx_data):
    #data is given in the dict format shown abov
    #idx_data is given as a string as shown above

    dataset = data['dataset']
    start = data['start']
    end = data['end']

    #setup stock and index datasets
    data = pd.read_csv(dataset,delimiter=',',header=None)
    idx = pd.read_csv(idx_data, delimiter=',',usecols=[0,1,4])

    #properly index index with right date range
    idx.set_index(['Date'])
    mask_sp = (idx['Date'] > start) & (idx['Date'] <= end)
    idx = idx.loc[mask_sp]

    idx["Price Relative"] = idx["Close"].astype(float)/idx["Open"].astype(float)
    del idx["Close"]
    del idx["Open"]

    betas = pd.DataFrame()

    for col in data.columns:
        print (col)
        temp = idx.copy()
        temp.reset_index(drop=True,inplace=True)
        temp["Stock"] = data[col]

        col_betas = []

        for day in range(beta_range):
            col_betas.append(1.0) #set all betas before calculation to one

        for day in range(beta_range,len(temp)):
            date_range = temp[day-beta_range:(day+1)]
            #Date range to use for calculating beta. Is last x days, where x is the beta_range specified above.
            cov_matrix = date_range.cov()
            beta = cov_matrix["Price Relative"][1]/cov_matrix["Price Relative"][0]
            col_betas.append(beta)
        betas[col] = col_betas
    return betas
