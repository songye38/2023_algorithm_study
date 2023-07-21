import sys
from itertools import combinations


n,m = map(int,input().split())
A = A = list(map(int,input().split()))
S = []
C = [0] * n
answer = 0

print("original")
print(S)
print(C)


temp = 0
for i in A:
    temp += i
    S.append(temp)


for i in range(n):
    remainder = S[i] % m #1,0,0, 1,0
    if remainder==0:
        answer += 1
    else:
        C[remainder] += 1
        
for i in range(m):
    answer += C[i] * (C[i]-1)/2)
