import numpy as np
import pandas as pd
from get_betas import *

#Only purpose of this file is to generate data, so it's written as a script
#not a function.

#beta date ranges to test
#These ranges are the number of trading days in
#1, 2, 3, 6, and 12 months
beta_ranges = [21, 42, 63, 126, 252]

for beta_range in beta_ranges:
    betas = getBetas(beta_range = beta_range)
    name = "../Data/nyse-o_betas_" + str(beta_range) + ".csv"

    betas.to_csv(name)
