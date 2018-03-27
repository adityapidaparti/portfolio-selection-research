import pandas as pd
import numpy as np
from sparse_port_admm import sparse_port_admm as spa
# import matplotlib.pyplot as plt

# This is our main function wrapper. It's going to perform setup for each
# test we do. That is, once we run this function, our initial paramters have
# been inputted and will stay that way (i.e. the learning rate and the L1 norm)
# It's going to come in the form of a function return results in the form of
# a pandas dataframe and a dictionary with all the parameters
#
# pricesData is the price relative matrix, a string to its location
# (default is '../Data/nyse-o.csv',)
# betasData is the beta dataset, a string to its location
# (default is '../Data/nyse-o_betas_21.csv')
# eta is learning rate (not varied, for now)
# alpha is L1 norm weight
# gamma is transaction cost
# maxRisk is max portfolio risk
# modes: reject will reject too risky of portfolios,
# if debug is True, print statements will appear

def lazy_updates_admm(pricesData='../Data/nyse-o.csv',betasData='../Data/nyse-o_betas_21.csv', \
    eta = 0.05, alpha = 0.01, gamma = 0.0 ,maxRisk = 10 ** 10, mode = "reject", debug = False):
    r = .01 #Augmentation term
    b = 2 #weight on L2 norm

    #Data setup
    prices = np.transpose(pd.read_csv(pricesData,sep=',',header=None).as_matrix())
    betas = pd.read_csv(betasData,delimiter=',',index_col=0).as_matrix()

    #Variable initialization
    (num_stock, num_days) = prices.shape
    weight = np.zeros(prices.shape)
    wealth = np.zeros((num_days, 1))
    portfolioBetas = np.zeros((num_days, 1))
    wealth[0,0] = 1 # Start with 1 dollar on day 1

    #portfolio for 1st day, allocate wealth equally across assets
    weight[0:, 0] = np.ones(num_stock) * (1/num_stock)
    #assign first day portfolio betas

    #debugging
    portfolioBetas[0,0] = np.dot(betas[0], weight[0:,0])

    #2nd through last day
    for day in range(1, num_days):

        if (debug):
            print("Day %d, Wealth: %f, Risk: %f" % (day, wealth[day-1,0], portfolioBetas[day-1, 0]))

        prev_day_weight = weight[:, day-1]
        prev_day_data = prices[:, day-1]

        if (mode == "reject" or mode == "original"):
            day_betas = betas[day]
            genPortfolio = spa(prev_day_weight, prev_day_data, eta, b, alpha, r)
            portfolioRisk = np.dot(day_betas, genPortfolio)
            if (portfolioRisk <= maxRisk and mode == "reject"):
                w = genPortfolio
            else:
                w = prev_day_weight

        elif(mode == "optimize"):
            raise NotImplementedError()
        else:
            raise RuntimeError()

        weight[:, day] = w
        new_wealth = wealth[day-1, 0] * np.dot(weight[:, day], prices[:, day])

        #Apply transaction cost.
        transaction_cost = gamma*abs(wealth[day-1, 0])*np.linalg.norm(weight[:,day-1]-weight[:,day],1)
        wealth[day, 0] = new_wealth - transaction_cost

        portfolioBetas[day,0] = portfolioRisk

    # if debug:
    #     plt.plot(portfolioBetas[0:day])
    #     title = "Risk over time \nmaxRisk: %f, eta: %f, alpha: %f" % (maxRisk, eta, alpha)
    #     plt.title(title)
        # plt.show()

    #to get most relevant values, access np.amax(portfolioBetas and wealth[5650, 0]
    return (portfolioBetas, wealth)
