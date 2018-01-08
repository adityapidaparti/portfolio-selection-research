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

def sparse_port_admm(w_t, x_t, eta, beta, gamma, rho, debug = False):

    #Parameters
    QUIET    = 1
    MAX_ITER = 1000 #Default 1000
    ABSTOL   = .0001 #Default .0001
    RELTOL   = .01 #Default .01
    n = len(w_t)
    w = np.zeros(n)
    z = np.zeros(n)
    u = np.zeros(n)

    #equal to the sum of each weight multiplied by its price relative
    const = np.dot(w_t, x_t)

    for k in range(MAX_ITER):
        #iterating through 3 sub problems until convergence or max iterations

        #W-update (portfolio update))
        w_temp = (eta/((rho+beta)*const))*x_t + w_t + (rho/(rho+beta))*z - (rho/(rho+beta))*u
        w = find_y(w_temp, 1) #projects onto a probablility distribution of size 1

        #Z-update
        #Similar to W-update
        z_old = z
        threshold = gamma/rho

        z_temp = (w - w_t + u)
        z = shrinkage(z_temp, threshold)

        #U-update, last step
        u += (w - w_t - z)

        #Computing primal and dual residual
        #Stopping criteria/convergence
        r_norm = la.norm(w - w_t - z) #shoud we replace this with u?
        s_norm = la.norm(-rho* (z - z_old));

        eps_pri = (n**.5) * ABSTOL + RELTOL * max(la.norm(w), la.norm(-w_t), la.norm(-z))
        eps_dual = (n**.5) * ABSTOL + RELTOL * la.norm(rho*u)

        if not QUIET:
            print ('---- ITER %d ----' % (k+1))
            print ("w:", w)
            print ("z:", z)
            print ("u:", u)
            print (la.norm(w),la.norm(-w_t),la.norm(-z))
            print (r_norm, eps_pri, s_norm, eps_dual)

        #Stopping criterion (close enough to optimum solution)
        if (r_norm < eps_pri and s_norm < eps_dual):
            if debug == True:
                print ("---STOPPING  ON ITER %d---" % (k+1))
            return w
    # print ("---STOPPING  ON ITER %d---" % (k+1))
    return w
