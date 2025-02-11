from math import *
a,b=list(map(int,input().split()))
maxi=max(a,b)
c=6-maxi+1
if 6%c==0:
    print(str(1)+"/"+str(6//c))
else:
    print(str(c//gcd(c,6))+"/"+str(6//gcd(c,6)))
