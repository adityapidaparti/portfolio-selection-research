#######################################################################
# Inputs: w_t   - portfolio for the previous day
#         x_t   - price relative for the previous day
#         eta   - weight on the log term
#         beta  - weight on the l-2 term
#         gamma - weight on the l-1 term
#         rho   - weight on the augmented lagrangian
# Outputs: w -  portfolio for the next day or w_t+1
#
# Authors: Nicholas Johnson and Puja Das (University of Minnesota)
# Converted from MATLAB to Python 3 by Aditya Pidaparti (University of Minnesota)
###########################################################################

import numpy as np
from numpy import linalg as la
from supporting_funcs import find_y, shrinkage

def sparse_port_admm(w_t, x_t, eta, beta, gamma, rho):

    #Inputs
    QUIET    = 1
    MAX_ITER = 1000
    ABSTOL   = 1e-4
    RELTOL   = 1e-2
    n = len(w_t)
    w = np.zeros(n)
    z = np.zeros(n)
    u = np.zeros(n)

    #equal to the sum of each weight multiplied by its price relative
    const = np.dot(w_t, x_t)
    # print ("w_t: ", w_t)
    # print ('x_t: ', x_t)
    # print ("const: ", const)

    #debugging
    count = 0
    fin = -1

    for k in range(MAX_ITER):
        #iterating through 3 sub problems until convergence or max iterations

        #W-update (portfolio update))
        w_temp = (eta/((rho+beta)*const))*x_t + w_t + (rho/(rho+beta))*z - (rho/(rho+beta))*u
        w = find_y(w_temp, 1) #projects onto a probablility distribution of size 1

        # print ("sparse w:", w)
        #Z-update
        #Similar to W-update

        #Z-update in Python is off from MATLAB quantities ever so slightly,
        #My guess right now is that it's due to floating point numbers
        #However, considering how accurate the values are, I'm leaving this for now
        z_old = z
        threshold = gamma/rho
        # print ("w", w)
        z_temp = (w - w_t + u)
        # print("z_temp is: ", "threshold is: ", threshold)
        z = shrinkage(z_temp, threshold)
        # count += 1
        # print (z)
        # if count == 3:
        #     raise Exception

        #U-update
        #Last step
        u += (w - w_t - z)
        # count += 1
        # print ("u: ", u)
        # if count == 3:
        #     raise Exception

        #Computing primal and dual residual
        #Stopping criteria/convergence
        r_norm = la.norm(w - w_t - z) #shoud we replace this with u?
        s_norm = la.norm(-rho* (z - z_old));

        eps_pri = (n**.5) * ABSTOL + RELTOL * max(la.norm(w), la.norm(-w_t), la.norm(-z))
        eps_dual = (n**.5) * ABSTOL + RELTOL * la.norm(rho*u)

        if not QUIET:
            print (r_norm, eps_pri, s_norm, eps_dual)

        #Stopping criterion (close enough to optimum solution)
        if (r_norm < eps_pri and s_norm < eps_dual):
            # print ("---STOPPING  ON ITER %d---" % (k+1))
            return w

    # print ('---STOPPING ON ITER %d---' % fin)
