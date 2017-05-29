import pandas as pd
import numpy as np
from datasets import *
import matplotlib.pyplot as plt
from lazy_updates_admm import lazy_updates_admm as lua

#Parameters we'll be varying:
#learning rate/eta: logarithmic increase from 10 ^ -6 to 10^2
#l1 norm weight/alpha
#transaction cost/gamma
#risk tolerance/max_vol
#beta window

#Note to self (Aditya Pidaparti): Likely the most important relationships
#will be transaction cost and risk tolerance as inputs, measuring return as an output
for h in range(-6,3): #h is eta, which is weight on log
    for a in range(-6,3): #a is alpha, which is weight on L1 norm
        for i in [.5,1,1.5]:
            results = lua(eta = 10**h, alpha = 10 ** a, maxRisk=i)
            print ("Eta: %f, Alpha: %f, maxRisk: %f, Wealth: %f" % (results[0], results[1], results[5], results[6]))
