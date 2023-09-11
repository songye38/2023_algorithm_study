import math

N  = int(iput())
A = [0] * (N+1)

for i in range(2,10000001):
    A[i] = i

for i in range(2,int(math.sqrt(N))+1):
    if A[i]==0:
        continue
    for j in range(i+i,N+1,i):
        A[j] = 0

def palindron(n):
    
