#Modify the code below so that the function sense, which 
#takes p and Z as inputs, will output the NON-normalized 
#probability distribution, q, after multiplying the entries 
#in p by pHit or pMiss according to the color in the 
#corresponding cell in world.


p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red','red','green'] # measurement 
pHit = 0.6
pMiss = 0.2

def sense(p, measurements):
    #
    #ADD YOUR CODE HERE
    q = []
    for i in range(len(p)):
       hit = (measurements == world[i]) 
       q.append(p[i]*(hit*pHit + (1-hit)*pMiss))  ##posterior prior probability * measurement likelyhood
    sump = sum(q)
    for i in range(len(p)):
       q[i] = q[i]/sump
    #
    return q

# after multiple measurements
for i in range(len(measurements)):
   p = sense(p,measurements[i])
   print p

import numpy as np
print np.argmax(p)
