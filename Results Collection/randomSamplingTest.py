import pandas as pd
import numpy as np
import random
from lazy_updates_admm import lazy_updates_admm as lua
from datetime import datetime

NYSE_DATASET="='../Data/nyse-o.csv"
BETA_RANGES = [21, 42, 63, 126, 252]
ALPHAS = [x/20. for x in range(0,9)]
GAMMAS = [0.0, 0.001, 0.0025, 0.005, 0.01]
ETAS = [x/10. for x in range(0,16,)]
MAX_RISKS = [x/20. for x in range(10,30)]

# Make modular for S&P500 dataset
def randomSampleNYSE(mode, debug=False):
    if debug:
        random.seed(0)  # use to get consistent results when testing.
    beta_range = random.choice(BETA_RANGES)
    beta_data = "../Data/nyse-o_betas_" + str(beta_range) + ".csv"
    alpha = random.choice(ALPHAS)
    gamma = random.choice(GAMMAS)
    eta = random.choice(ETAS)
    max_risk = random.choice(MAX_RISKS)

    print("beta_range: %d, gamma: %f, alpha: %f, eta: %f,max_risk: %f" %
        (beta_range, gamma, alpha, eta, max_risk))

    (portBetas, wealth) = lua(betasData=beta_data, eta=eta,alpha = alpha, gamma = gamma,
    maxRisk = max_risk, mode = mode, debug=debug)
    return [beta_range, alpha, gamma, eta, max_risk, wealth[5650, 0]]

def randomSamplingNYSE(num_tests=100, mode='reject', debug=False):
    results = np.zeros((num_tests, 6))
    for i in range(num_tests):
        results[i] = randomSampleNYSE(mode, debug)

    results = pd.DataFrame(results)
    results.columns = ['Beta Range', 'Alpha', 'Gamma', 'Eta', 'Max Risk', 'Wealth']
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    results.to_csv("../Rejection/" + str(num_tests) + "_" + time)

randomSamplingNYSE()
