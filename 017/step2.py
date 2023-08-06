import sys


A = list(input())

#단순 출력
for i in range(len(A)):
    print(A[i])


for i in range(len(A)):
    Max = i #42 
    for j in range(i+1, len(A)):
        if A[j] > A[Max]:
            Max = j #max의 인덱스 값 바꿔주기 

        if A[i] < A[Max]:
            temp = A[i]
            A[i] = A[Max]
            A[Max] = temp