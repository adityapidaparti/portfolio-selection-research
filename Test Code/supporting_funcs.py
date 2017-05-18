import numpy as np

def find_y(v,z): #projection to simplex
    mu = np.sort(v)[::-1] #sort in descending order'
    rho = 1
    # print ("mu: ", mu)
    for j in range(1,(len(mu)+1)):
        residual = mu[j-1] - ((sum(mu[:j]) - z)/(j))
        if (residual > 0):
            rho = j

    theta = (sum(mu[0:(rho)])-z)/rho

    new_v = v
    for i in range(len(new_v)):
        new_v[i] = max(new_v[i]-theta, 0)
    return new_v

def shrinkage(x, kappa):
    #what is the point of this function???

    # print ('x is:', x, 'kappa is:', kappa)
    z = np.maximum(0, x-kappa) - np.maximum (0, -x-kappa)
    # print ("shrinkage z: ", z)
    return z
