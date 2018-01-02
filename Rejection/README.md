Data collection function - run each time using different dataset
Lazy updates function - same as before
Sparse updates function - same as before
Supporting functions - same as before
Debugging function - have one for lazy updates and sparse updates
 -sends outputs to csv, plots w/ seaborn
 Plotting functions - build the 3d graph nick had, and the risk vs return one pooja had


Situations to test:
-Vary learning rate (eta)
-Vary transaction cost (gamma)
-Vary L1 norm weight (alpha)
-Vary risk tolerance (known as the beta, but as it's used, I will use vol to measure it as volatility)

Steps: (do for NYSE and S&P 500 datasets)
1a. Obtain data (price relatives and betas for each day)
1b. Setup testing suite. Develop Lazy and Sparse w/ parameters to include betas.
2. Observe the risk variation without any parameters (implement computing the stock beta)
3. Using a good learning rate and l1 norm, with no transaction cost, observe portfolio return as a function.
4. Test the following algorithm methods:
  -If a portfolio's beta is too large, reject the portfolio
  -Weight each stock to make riskier stocks worth more costly in the cost function.
    -when portfolio beta is too large, square all betas to re-emphasize less risky stocks
5. Find good parameters to run the larger simulation
  -Ranges of learning rate, transaction cost, L1 norm, and risk
6. Do a nested for loop 4 levels deep. Test and save results
7. Look for interesting points in results. Make pretty graphs.
8. Write report


Note:
Potential method of risk testing if time:
Set a maximum risk value, and if portfolio value exceeds that risk
recompute with the inherent volatilities squared to emphasize
less volatile stocks over more volatile stocks


Steps to optimize stocks
-If current portfolio suggestion is over maximum risk
-Project onto L1 ball
-Project onto simplex (use find_y function as a model)
-Alternate between the previous two until a portfolio is found within the feasible set

Notes: Use Proximal Algorithms by Parikh and Boyd, sections 6.3.2 and 6.5.2.
-For 6.5.2, lambda is the size of the l1 ball
-For 6.3.2, a is the betas, v is portfolio
-For 6.3.2, ()_+ corresponds to finding the maximum or zero, whichever is larger.