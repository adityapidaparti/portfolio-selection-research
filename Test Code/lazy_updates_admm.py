import numpy as np
import sparse_port_admm as spa
import datasetup
import pandas as pd

#This is our main function wrapper. It's going to perform setup for each
#test we do. That is, once we run this function, our initial paramters have
#been inputted and will stay that way (i.e. the learning rate and the L1 norm)
#It's going to come in the form of a function return results in the form of
# a pandas dataframe and a dictionary with all the parameters

#Parameters we'll be varying:
#learning rate/eta: logarithmic increase from 10 ^ -6 to 10^2
#l1 norm weight/alpha
#transaction cost/gamma
#risk tolerance/max_vol
#beta window
