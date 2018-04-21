# Hyperparameters and constants that are widely used are defined here.

# Coarse Hyperparameters for nyse-o dataset
nyse_o_hyperparameters = {
	'beta_ranges' : [21, 42, 63, 126, 252],
	'alphas' : [x/20. for x in range(0,9)],
	'gammas' : [0.0, 0.001, 0.0025, 0.005, 0.01],
	'etas' : [x/10. for x in range(0,16,)],
	'max_risk' : [x/20. for x in range(10,30)]}

# Coarse Hyperparameters for sp500 dataset
sp500_hyperparameters = {
	'beta_ranges' : [21, 42, 63, 126, 252],
	'alphas' : [x/10. for x in range(0,4)],
	'gammas' : [0.0, 0.001, 0.0025, 0.005, 0.01],
	'etas' : [x/1. for x in range(8,32)],
	'max_risk' : [x/20. for x in range(10,30)]}

# Fine hyperparameters for nyse-o dataset, low betas
nyse_o_low_betas = {
	'beta_ranges' : [21, 42, 63, 126, 252],
	'alphas' : [x/20. for x in range(0,9)],
	'gammas' : [0.0, 0.001, 0.0025, 0.005, 0.01],
	'etas' : [x/10. for x in range(0,16,)],
	'max_risk' : [x/20. for x in range(8,20)]}
if __name__ == '__main__':
	raise NotImplementedError()