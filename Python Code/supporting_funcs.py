import numpy as np

def find_y(v,z): #projection to simplex
    mu = np.sort(v)[::-1] #sort in descending order
    for j in range((len(mu))):
        residual = mu[j] - ((sum(mu[0:(j+1)]) - z)/(j+1))
        # print ("Mu shape: ", mu.shape)
        rho = 1
        if (residual > 0):
            rho = j+1

    theta = (sum(mu[0:(rho+1)])-z)/rho
    # print (mu[0:(rho+1)])
    # print ('rho: ', rho)
    # print ("sum: ", sum(mu[0:(rho+1)]))

    new_v = v
    for i in range(len(new_v)):
        new_v[i] = max(new_v[i]-theta, 0)
    # new_v = np.amax(v-theta, 0)
    # print (new_v)
    return new_v

def shrinkage(x, kappa):
    #what is the point of this function???

    print ('x is:', x, 'kappa is:', kappa)
    z = np.maximum(0, x-kappa) - np.maximum (0, -x-kappa)
    print ("shrinkage z: ", z)
    return z
