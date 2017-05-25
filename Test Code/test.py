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
