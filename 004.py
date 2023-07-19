import sys


###############################################
# TODO
#! alert comment
# * important comment
# ? 궁금한 것들
###############################################


###############################################
#* step1 입력받고 원본 배열 만들기
#* step2 부분합 배열 만들기
#* step3 부분구간 합 만들기
###############################################



#* STEP1 입력받기 
input = sys.stdin.readline
n,m = list(map(int,input().split()))

A_matrix = [] #원본 데이터를 담은 배열 

#? 배열을 이렇게 담아놓는게 맞나?
D_matrix = [[0] * n] * n  #구간합 데이터를 담은 배열 


#* 입력받아 원본 배열 만들기 
for i in range(n):
    lines = list(map(int,input().split()))
    A_matrix.append(lines)

print("원본 배열 A_matrix")
print(A_matrix)


#* STEP2 구간 부분배열 만들기 
#? 구간 부분 배열을 이렇게 두 부분으로 나누어서 하는게 맞나?
column_temp = 0
row_temp = 0

for i in range(n):
    column_temp += A_matrix[0][i]
    D_matrix[0][i] = column_temp

    row_temp += A_matrix[i][0]
    D_matrix[i][0] = row_temp


D_matrix = [[1,3,6,10],[3,0,0,0],[6,0,0,0],[10,0,0,0]] #가정하기 
#1행과 1열을 제외한 나머지 부분 구간 부분합 구하기 
for i in range(1,n):
    for j in range(1,n):
        D_matrix[i][j] = D_matrix[i][j-1] + D_matrix[i-1][j] - D_matrix[i-1][j-1] + A_matrix[i][j]

print("first line 합 배열")
print(D_matrix)


#*STEP3 구간 부분합 구하기 
#입력받아 원본 배열 만들기 
for i in range(m):
    x1,y1,x2,y2 = list(map(int,input().split())) 
    result = D_matrix[x2][y2] - D_matrix[x1-1][y2] - D_matrix[x2][y1-1] + D_matrix[x1-1][y1-1]
    print(result)