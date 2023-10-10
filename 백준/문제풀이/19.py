#sudo

N,K = map(int, input().split())
A = [0] * N

def quick_sort(S,E,K):
    global A
    pivot = find_pivot(S,E)
    if pivot == K: 
        return
    elif K < pivot : quick_sort(S,pivot-1,K)
    else : quick_sort(pivot+1,E,K)

    


def swap(i,j):
    global A
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


def find_pivot(S, E):
    global A #생각하지 못함. 
    if S - E ==1: #데이터가 2개만 있는 경우
        if A[S] > A[E]:
            swap(S,E)

    #pivot의 index 구하기 
    M = S + E //2 #median index

    #제일 앞에 있는 값과 바꾸기
    swap(S,M)

    #피봇 자체의 인덱스를 start index로 해주기 
    pivot = A[S]
    i = S + 1
    j = E


    while i<=j:
        while A[i] < A[pivot]:
            i+=1
        while A[j] > A[pivot]:
            j-=1;
        
        swap(i,j)

    A[i] = A[pivot]
    return i

