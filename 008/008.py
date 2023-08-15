n = int(input())
result = 0
A = list(map(int,input().split()))
A.sort()

for k in range(len(n)):
    find = A[k]
    i = 0
    j = k-1

    while i < j:
        if A[i] + A[j] ==find:
            p
        elif A[i]+A[j] < find:
            i+=1
        else:
            j-=1
