import pandas as pd
import numpy as np
import random
from lazy_updates_admm import lazy_updates_admm as lua
from datetime import datetime
import sys
import os
import pathlib
import multiprocessing 
from functools import partial

scriptPath = os.path.realpath(os.path.dirname(sys.argv[0]))
os.chdir(scriptPath)
sys.path.append("..")
import constants

"""
These are hyperameters to be set. Random samples will be taken form these
values. Their default values are specified in constants.py.

TODO: Test the range of low max risk. Large variability right now, so requires
more insight.
"""
# BETA_RANGES = [21, 42, 63, 126, 252]
# ALPHAS = [x/20. for x in range(0,9)]
# GAMMAS = [0.0, 0.001, 0.0025, 0.005, 0.01]
# ETAS = [x/10. for x in range(0,16,)]
# MAX_RISKS = [x/20. for x in range(10,30)]

"""
Top level function that executes a generalized testing suite of cascading
functions.

@param num_tests the number of tests to run.
@param mode only reject is available currently
@param dataset 'nyse' or 'sp500' available right now.
@param debug is a flag for verbose debug statements.
"""
def randomSampling(num_tests=100, mode='reject', dataset='nyse-o', \
	hyperparameters={}, debug=False):
	if mode != 'reject':
		raise NotImplementedError()

	# If hyperparameters are not specified, then use the default ones specified
	# in constants.py
	if dataset == 'nyse-o' and not hyperparameters:
		hyperparameters = constants.nyse_o_hyperparameters
	elif dataset == 'sp500' and not hyperparameters:
		hyperparameters = constants.sp500_hyperparameters

	results = np.zeros((num_tests, 7))
	for i in range(num_tests):
		result = singleRandomtest(mode, dataset, hyperparameters, debug)
		results[i] = result

	results = pd.DataFrame(results)
	results.columns = ['Beta Range', 'Alpha', 'Gamma', 'Eta', 'Max Risk', \
	'Wealth', 'No Risk Wealth']

	time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
	file_directory = "../rejection/" + dataset + "/compare_" + str(num_tests)

	if debug:
		file_directory += "-debug"

	try:
		pathlib.Path(file_directory).mkdir(parents=True)
	except OSError:
		pass
	results.to_csv(file_directory + "/" + time + ".csv")
	

"""
Runs a single random test. Fairly coupled as the parameters are hardcoded above
at the top of this file. However, as these hyperparameters are tuned in a
manual way and don't have to scale, this is left hard-coded.

@param mode Only can be 'reject'. Unused.
@param dataset Either 'nyse-o' or 'sp500'
@param hyperparameters allows to pass in ideal hyperparameters from
@param debug allwos for verbose and nonrandom results to be generated.
"""

def singleRandomtest(mode, dataset, hyperparameters, debug):
	if debug:
		random.seed(0)

	dataset_file = "../Data/" + dataset + ".csv"
	beta_window = random.choice(hyperparameters['beta_ranges'])

	# Example full filename: "../Data/nyse-o_betas_126.csv"
	betas_file = "../Data/" + dataset + "_betas_" + str(beta_window) + ".csv"
	alpha = random.choice(hyperparameters['alphas'])
	gamma = random.choice(hyperparameters['gammas'])
	eta = random.choice(hyperparameters['etas'])
	max_risk = random.choice(hyperparameters['max_risk'])

	print("beta_range: %d, gamma: %f, alpha: %f, eta: %f,max_risk: %f" %
        (beta_window, gamma, alpha, eta, max_risk))

	# Run with risk limitation
	(portfolio_betas, risk_limit_wealth) = lua(dataset_file, betas_file, \
		eta, alpha, gamma, max_risk, mode, debug)

	# Run with no risk limitation
	(no_risk_betas, no_risk_wealth) = lua(dataset_file, betas_file, \
		eta, alpha, gamma, float("inf"), mode, debug)

	last_day = risk_limit_wealth.shape[0] - 1
	return [beta_window, alpha, gamma, eta, max_risk, \
	risk_limit_wealth[last_day,0], no_risk_wealth[last_day,0]]


def fine_grid_driver_nyse():
	hp_s = {
		'beta_ranges' : [21, 63, 126],
		'alphas' : [0.5, 0.7, 0.9, 1.1, 1.3],
		'gammas' : [0.0, 0.0025, 0.01],
		'etas' : [0.04, 0.08, 0.1, 0.15, 0.2, 0.3],
		'max_risk' : [0.5, 0.7, 0.9, 1, 1,2]
	}
	# nyse_func = partial(randomSampling, num_tests=1, debug=True, dataset='nyse-o', hyperparameters=hp_s)
	proccesses = [multiprocessing.Process(
			target=partial(
				randomSampling, 
				num_tests=1, 
				debug=False,
				dataset='nyse-o',
				hyperparameters=hp_s)
			) 
			for x in range(20)]

	for process in proccesses:
		process.start()

	for process in proccesses:
		process.join()


def fine_grid_driver_sp500():
	proccesses = [multiprocessing.Process(
			target=partial(
				randomSampling, 
				num_tests=1, 
				debug=False,
				dataset='sp500',)
			) 
			for x in range(50)]

	for process in proccesses:
		process.start()

	for process in proccesses:
		process.join()
	

if __name__ == '__main__':
	# randomSampling(num_tests=1, debug=False, dataset='sp500')
	# sp500_fnc = partial(randomSampling, num_tests=1, debug=True, dataset='sp500')
	# proccesses = [multiprocessing.Process(target=partial(randomSampling, num_tests=10, debug=False, dataset='sp500')) for x in range(10)]

	# fine_grid_driver_nyse()
	fine_grid_driver_sp500()

