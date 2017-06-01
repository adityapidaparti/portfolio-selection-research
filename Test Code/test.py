import pandas as pd
import numpy as np
from datasets import *
import matplotlib.pyplot as plt
from lazy_updates_admm import lazy_updates_admm as lua
import pandas as pd

#Parameters we'll be varying:
#learning rate (eta)
#l1 norm weight (alpha)
#transaction cost (gamma)
#risk tolerance (maxRisk)
#beta window (beta_range)

#Note to self (Aditya Pidaparti): Likely the most important relationships
#will be transaction cost and risk tolerance as inputs, measuring return as an output

def testOne(startpt = 0,mode='reject'):
    maxRisks = [x/10 for x in range(5,16)] #Range: .5 to 1.5, num_iters: 10
    etas = [x/10 for x in range(1,21,2)] #Range: .1 to 2.0, by .2, num_iters: 10
    alphas = [x/20 for x in range(1,9)] #Range: .05 to 0.4, num_iters: 8
    gammas = [0.0, 0.001, 0.0025, 0.005, 0.01] #num_iters: 5 #NOTE: Accidentally skipped no transaction cost.
    beta_ranges = [21, 42, 63, 126, 252] #num_iters: 5
    #Total:

    # resultFile = "/Results/testOne.csv"
    dimension = (len(maxRisks)*len(etas)*len(alphas)*len(gammas)*len(beta_ranges))
    results = np.zeros((20,6))

    index = 0
    savept = 0
    for maxRisk in maxRisks:
        for eta in etas:
            for alpha in alphas:
                for gamma in gammas:
                    for beta_range in beta_ranges:
                        if startpt <= index:
                            print ("maxRisk: %f, eta: %f, alpha: %f, gamma: %f, beta_range: %d" % (maxRisk, eta, alpha, gamma, beta_range))
                            betasData = "../Data/nyse-o_betas_" + str(beta_range) + ".csv"
                            wealth = lua(betasData = betasData, eta = eta, alpha = alpha, gamma = gamma, maxRisk = maxRisk, mode = mode)
                            print ("Wealth: %f, Index:%d" % (wealth,index))

                            results[savept] = [eta, alpha, gamma, beta_range, maxRisk, wealth]
                            savept = savept + 1
                            if savept == 100: #Save results for all gammas and beta_ranges for given maxRisk, eta, and alpha
                                results = pd.DataFrame(results)
                                results.to_csv('./Results/'+str(maxRisk)+"_"+str(eta)+"_"+str(alpha)"_"+str(gamma)"_"+str(beta_range)"_"+'.csv')
testOne()
