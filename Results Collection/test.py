import pandas as pd
import numpy as np
from datasets import *
import matplotlib.pyplot as plt
from lazy_updates_admm import lazy_updates_admm as lua
import sys

# Parameters we'll be varying:
# learning rate (eta)
# l1 norm weight (alpha)
# transaction cost (gamma)
# risk tolerance (maxRisk)
# beta window (beta_range)

def testOne(startpt, mode='reject'):
    beta_ranges = [21, 42, 63, 126, 252]
    gammas = [0.0, 0.001, 0.0025, 0.005, 0.01]
    alphas = [x/20 for x in range(1,9)] # Range: .05 to 0.4, 8 iterations
    etas = [x/10 for x in range(1,21,2)] # Range: .1 to 2.0, by .2, 10 iterations
    maxRisks = [x/10 for x in range(6,16)] # Range: .6 to 1.5, 10 iterations


    num_tests = 100
    results = np.zeros((num_tests,6))

    index = 0
    savept = 0
    for beta_range in beta_ranges:
        for gamma in gammas:
            for alpha in alphas:
                for eta in etas:
                    for maxRisk in maxRisks:
                        if startpt <= index:
                            print ("beta_range: %d, gamma: %f, alpha: %f, eta: %f,maxRisk: %f" % (beta_range, gamma, alpha, eta, maxRisk))
                            betasData = "../Data/nyse-o_betas_" + str(beta_range) + ".csv"
                            wealth = lua(betasData = betasData, eta = eta, alpha = alpha, gamma = gamma, maxRisk = maxRisk, mode = mode)
                            print ("Wealth: %f, Index:%d" % (wealth,index))

                            results[savept] = [eta, alpha, gamma, beta_range, maxRisk, wealth]
                            savept = savept + 1
                            index = index + 1
                            if savept == num_tests: # Save results for all gammas and beta_ranges for given maxRisk, eta, and alpha
                                results = pd.DataFrame(results)
                                results.to_csv('./Results/'+str(startpt)+"_"+str(beta_range)+"_"+str(gamma)+"_"+str(alpha)+'.csv')
                                return
                        else:
                            index = index + 1
arg = sys.argv[1]
testOne(int(arg))
