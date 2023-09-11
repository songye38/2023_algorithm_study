#sudo

N = int(input())
A = list(input().split()) #list(map(int,input().split()))
S = [0] * N





for i in range(1,N):
    insert_point = i
    for j in range(i-1, -1,-1):
        if A[insert_point] < A[j]:
            insert_point = j
    for j in range(i,insert_point+1, -1):
        A[j] = A[j-1]
    A[insert_point] = A[i]

    
S[0] = A[0]

# 합배열 만들기
for i in range(1,N):
    S[i] = S[i-1] + A[i]


sum = 0
for i in range(S):
    sum += S[i]

print(sum)
