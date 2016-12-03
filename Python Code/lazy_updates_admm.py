import numpy as np
# from compute_PRM import compute_PRM, compute_from_csv
from sparse_port_admm import *
from pandas import read_csv
import matplotlib.pyplot as plt

#Lazy updates Algorithm
#PRM = Price relative matrix of dimensions num_days x num_stock (numpy array)
#eta is the learning rate (value of 0.05 is good)
#weight is each day's portfolio

#Cleaning data, for tests only
data =  np.transpose(read_csv('nyse.csv', sep=',',header=None).as_matrix()) #test PRM

g = 0.0# Transaction cost
r = 0.1 # Augmentation term
b= 2 # Weight on L2 norm


def lazy_updates_admm(eta, alpha, PRM = data, gamma = g, rho = r, beta = b):
    print ('===================================================')
    print ("Eta: %f, Alpha: %f, Gamma = %f, Rho = %f, Beta = %f" % (eta, alpha, gamma, rho, beta))

    #Initialize variables
    (num_stock, num_days) = PRM.shape
    weight = np.zeros(PRM.shape)
    wealth = np.zeros((num_days, 1))
    wealth[0,0] = 1 # Start with 1 dollar

    #portfolio for 1st day, allocate wealth equally across assets
    weight[0:, 0] = np.ones(num_stock) * (1/num_stock)

    #2nd through last day
    # eta = .1
    # alpha = 0.000001
    for day in range(1, num_days):
        print("Day %d, Wealth: %f" % (day, wealth[day-1,0]))

        prev_day_weight = weight[:, day-1]
        prev_day_data = PRM[:, day-1]

        #ADMM
        w = sparse_port_admm(prev_day_weight, prev_day_data, eta, beta, alpha, rho)
        # print ("w: ", w)
        #updates

        weight[:, day] = w
        new_wealth = wealth[day-1, 0] * np.dot(weight[:, day], PRM[:, day])
        transaction_cost = gamma*abs(wealth[day-1, 0])*np.linalg.norm(weight[:,day-1]-weight[:,day],1)
        wealth[day, 0] = new_wealth - transaction_cost

        # if day % 100 == 0:
        #     print ("w: ", w)
        # if day == num_days or np.isnan(wealth[day,0]):
        #     print ("w: ", w)
        #     plt.plot(wealth[0:day])
        #     plt.show()
        #     raise RuntimeError('stop')

    print(wealth[num_days - 1, 0])
    raise RuntimeError('stop')
    # print (len(wealth), num_days)


for h in range(-6,3): #h is eta, which is weight on log
    for a in range(-6,3): #a is alpha, which is weight on L1 norm
        lazy_updates_admm(eta = 10.0**h, alpha = 10.0**a)
