import numpy as np
from compute_PRM import compute_PRM, compute_from_csv
import matplotlib.pyplot as plt

#EG Algorithm
#PRM = Price relative matrix of dimensions num_days x num_stock (numpy array)\
#eta is the learning rate (value of 0.05 is good)
#weight is each day's portfolio

def eg_Portfolio(PRM, eta):
	(num_days, num_stock) = PRM.shape
	weight = np.zeros(PRM.shape)
	wealth = np.zeros((num_days, 1))
	wealth[0,0] = 1 # Start with 1 dollar

	#portfolio for 1st day, allocate wealth equally across assets
	weight[0, 0:] = np.ones((1, num_stock)) * (1/num_stock)

	#2nd through last day
	for day in range(1, num_days):
		# print("Day %d" % day)
		prev_day_weight = weight[day-1, :]
		prev_day_data = PRM[day-1, :]

		#t is dot product of previous day weight and previous day data vectors
		t = np.dot(prev_day_weight, prev_day_data)

		#updates
		weight[day, :] = prev_day_weight * np.exp(eta * prev_day_data / t)
		weight[day, :] /= np.sum(weight[day, :])

		wealth[day, 0] = wealth[day-1, 0] * np.dot(weight[day, :], PRM[day, :])

	print (wealth)
	print (len(wealth), num_days)
	return wealth

#Testing
days_to_run = 3650/2 #roughly 10 years
PRM = compute_PRM(days_to_run)
eg_Portfolio(PRM, 0.05)

PRM = compute_from_csv('nyse.csv')
w = eg_Portfolio(PRM, 0.05)
