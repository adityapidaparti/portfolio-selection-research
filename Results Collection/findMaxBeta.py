from lazy_updates_admm import lazy_updates_admm as lua
import numpy as np

def findMaxBeta(pricesData, betasData, eta, alpha, gamma, debug):
    # import pdb; pdb.set_trace()
    (betas, wealth) = lua (pricesData, betasData, eta, alpha, gamma,
    mode = "original", debug = debug)

    return betas

betas = findMaxBeta('../Data/nyse-o.csv', '../Data/nyse-o_betas_21.csv',
0.05, 0.01, 0.00, False)

print(np.amax(betas))
