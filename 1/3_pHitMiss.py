#Write code that outputs p after multiplying each entry 
#by pHit or pMiss at the appropriate places. Remember that
#the red cells 1 and 2 are hits and the other green cells
#are misses.


p=[0.2,0.2,0.2,0.2,0.2]
pHit = 0.6
pMiss = 0.2

#Enter code here
p = [p[0]*pMiss , p[1]*pHit, p[2]*pHit, p[3]*pMiss , p[4]*pMiss]

print "before Normalization\n"
print p
print sum(p)
print "\n"

sump = sum(p)
for i in range(len(p)):
  p[i] = p[i]/sump

print "after Normalization\n"
print p
print sum(p)
