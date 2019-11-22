import numpy as np
import matplotlib.pyplot as plt
import sys

def ar_poly(p, delta = 0.1):
    
    roots = []
    
    # Number of complex roots
    n1 = np.random.choice(np.arange(p+1))
    
    while n1 % 2 != 0:
        n1 = np.random.choice(np.arange(p+1))
    
    # Number of real roots
    n2 = p - n1
    
    
    for i in range(n1//2):
        
        # Draw uniformly on (-1,1]
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        
        while (x**2 + y**2) > 1 or (x**2 + y**2) < delta**2:
            
            x = np.random.uniform(-1, 1)
            y = np.random.uniform(-1, 1)
            
        z = np.power(complex(x,y), -1)
        z_bar = np.conj(z)
        
        roots.append(z)
        roots.append(z_bar)
    
    for i in range(n2):
        
        r = np.random.uniform(-1,1)
        
        while abs(r) < delta:
            r = np.random.uniform(-1,1)
        
        roots.append(1/r)
        
    return roots

def ar_process(p, n, delta = 0.1):

    poly = np.real(np.polynomial.polynomial.polyfromroots(ar_poly(p)))
    
    poly = poly / poly[0]

    phi_vec = -1*poly[1:]

    phi_vec = np.flip(phi_vec)

    sample = np.zeros(p+n)

    for i in range(p, p+n):

        sample[i] = np.dot(phi_vec, sample[i-p:i]) + np.random.randn()

    return sample[p:]
    
def main():

    p = int(sys.argv[1])
    n = int(sys.argv[2])

    ar_obs = ar_process(p,n)
    plt.plot(range(len(ar_obs)), ar_obs)
    plt.show()

    return ar_obs

if __name__ == "__main__":

    main()
