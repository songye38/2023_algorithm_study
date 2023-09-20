N = int(input())
M = int(input())
dosi = [[[0] for j in range(N+1)] for i in range(N+1)] #다르게 만들것 같다. 

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a!=b:
        parent[b] = a

for i in range(1,N+1): #데이터 넣기 !!TODO
    dosi[i] = list(map(int,input().split()))
    dosi.insert(0,0)


#여기서 그냥 인풋으로 받기 
route = list(map(int,input().split()))
route.insert(0,0) #오 이건 새롭다


parent = [0] * (N+1)

for i in range(1,N+1): #대표노드 초기화
    parent[i] = i

for i in range(1,N+1):
    for j in range(1,N+1):
        if dosi[i][j] ==1:
            union(i,j)

index = find(route[1])

isConnect = True

for i in range(2,len(route)):
    if index !=find(route[i]):
        isConnect = False
        break

if isConnect:
    print("Yes")
else:
    print("NO")






