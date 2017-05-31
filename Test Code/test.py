import pandas as pd
import numpy as np
from datasets import *
import matplotlib.pyplot as plt
from lazy_updates_admm import lazy_updates_admm as lua

#Parameters we'll be varying:
#learning rate (eta)
#l1 norm weight (alpha)
#transaction cost (gamma)
#risk tolerance (maxRisk)
#beta window (beta_range)

#Note to self (Aditya Pidaparti): Likely the most important relationships
#will be transaction cost and risk tolerance as inputs, measuring return as an output

def testOne(mode='reject'):
    maxRisks = [x/10 for x in range(21)] #20
    etas = [x/10 for x in range(1,26)] #25
    alphas = [x/20 for x in range(1,11)] #10
    gammas = [x/1000 for x in range(1,10)] #10
    beta_ranges = [21, 42, 63, 126, 252] #5

    # resultFile = "/Results/testOne.csv"
    dimension = (len(maxRisks)*len(etas)*len(alphas)*len(gammas)*len(beta_ranges))
    results = np.zeros((100,6))

    index = 0
    savept = 0
    for maxRisk in maxRisks:
        for eta in etas:
            for alpha in alphas:
                for gamma in gammas:
                    for beta_range in beta_ranges:
                        print ("maxRisk: %f, eta: %f, alpha: %f, gamma: %f, beta_range: %f" % (maxRisk, eta, alpha, gamma, beta_range))
                        betasData = "../Data/nyse-o_betas_" + str(beta_range) + ".csv"
                        wealth = lua(betasData = betasData, eta = eta, alpha = alpha, gamma = gamma, maxRisk = maxRisk, mode = mode)
                        print ("Wealth: %f, Index:%f" % (wealth,index))

                        results[savept] = [eta, alpha, gamma, beta_range, maxRisk]
                        index = index + 1
                        savept = savept + 1
                        if savept == 100:
                            np.savetxt('/Results/'+str(index)+'.csv', results)
                            savept = 0
                            results = np.zeros((100,6))
testOne()
