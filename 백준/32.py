n, k = map(int,input().split())
A = [0] * n


for i in range(n):
   A[i] = int(input())

coin_count = 0

for i in range(n-1,-1,-1):
   if A[i] <=k:
      coin_count += int(k / A[i])
      k = k % A[i]

print(coin_count)


