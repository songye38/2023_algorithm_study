def merge(s,e):
    if e-s <1 : 
        return
    print("merging ",s,e)
    m = int(s + (e-s) /2)
    merge(s,m)
    merge(m+1,e)
    for i in range(s,e+1):
        tmp[i] = A[i]
    print("temp is",tmp)

    k = s
    index1 = s
    index2 = m+1
    print("index1 : ",index1)


N = int(input())
A = [0] * int(N+1)
tmp = [0] * int(N+1)

for i in range(1,N+1):
    A[i] = int(input())

merge(1,5)