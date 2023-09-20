N,M = map(int,input().split())
parent = [0] * (N+1)

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a !=b:
        parent[b] = a

def checkSame(a,b):
    a = find(a)
    b = find(b)
    if a==b:
        return True
    else:
        return False


for i in range(0,N+1): #대표노드 설정하기 
    parent[i] = i


#값 입력받고 결과 출력하기 
for i in range(M):
    query, set1,set2 = map(int,input().split())
    if query==0:
        union(set1,set2)
    else:
        if checkSame(set1,set2):
            print("yes")
        else:
            print("NO")

