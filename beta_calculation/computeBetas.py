import numpy as np
import pandas as pd
from get_betas import *
from constants import BETA_RANGES
from datasets import *

# Computes the maximum and minimum beta.
# Used and useful for debugging.
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

# Finds the betas for all days given a dataset of stock performance and 
def computeBetas(data, output_filename):
    for beta_range in BETA_RANGES:
        betas = getBetas(data, beta_range)
        betas.to_csv("../Data/" + output_filename + '_betas_' + 
            str(beta_range) + '.csv')

if __name__ == "__main__":
    computeBetas(sp500, 'sp500')