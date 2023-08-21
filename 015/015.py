#sudo

n = int(input())
A = [0] * n

for i in range(n):
    A[i] = int(input())


#print(A) #[5, 2, 3, 4, 1]

print("----------------------------------")
for i in range(n-1): #0,1,2,3,4
    for j in range(n-i-1):
        if A[j] > A[j+1]:
            temp = A[j]
            A[j] = A[j+1]
            A[j+1] = temp
    
for i in range(n):
    print(A[i])