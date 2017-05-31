import numpy as np
import pandas as pd
from get_betas import *

#Only purpose of this file is to generate data, so it's written as a script
#not a function.

#beta date ranges to test
#These ranges are the number of trading days in
#1, 2, 3, 6, and 12 months
beta_ranges = [21, 42, 63, 126, 252]
def computeBetas():
    for beta_range in beta_ranges:
        betas = getBetas(beta_range = beta_range)
        name = "../Data/nyse-o_betas_" + str(beta_range) + ".csv"

        betas.to_csv(name)

def computeExtremaBetas():
    results = []
    for beta_range in beta_ranges:
        betas = pd.read_csv("../Data/nyse-o_betas_" + str(beta_range) + ".csv")
        betas = betas.values
        currMax = -10 ** 10
        currMin = 10**10
        for r in range(len(betas)):
            for c in range(1,len(betas[r])):
                val = betas[r][c]
                if val > currMax:
                    print (val)
                    currMax = val
                if val < currMin:
                    currMin = val
        results.append((currMin, currMax))
    print (results)

computeExtremaBetas()
