import sys


# ###############################################
# # TODO
# #! alert comment
# # * important comment
# # ? 궁금한 것들
# ###############################################


# ###############################################
# #* 23.07.19(수)
# #* step1 입력받고 원본 배열 만들기
# #* step2 부분합 배열 만들기
# #* step3 부분구간 합 만들기
# ###############################################


 #* STEP1 입력받기 -----------------------------------------------------------------------------
input = sys.stdin.readline
n,m = list(map(int,input().split())) #! 굳이 리스트로 만들 필요가 없음. 

A_matrix = [] #원본 데이터를 담은 배열 

# #! 배열을 이렇게 담아놓는게 맞나?
D_matrix = [[0] * n] * n  #! 기본적으로 n개가 아니라 n+1개로 만들어야 했었다. 

D_matrix = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

# #* 입력받아 원본 배열 만들기 
for i in range(n):
    lines = list(map(int,input().split())) #! 여기서도 리스트가 필요없음. n+1개로 만들어 줬어야 했음. 
    A_matrix.append(lines)

print("원본 배열 A_matrix")
print(A_matrix)


# #* STEP2 구간 부분배열 만들기 -------------------------------------------------------------------
# #! 구간 부분 배열을 이렇게 두 부분으로 나누어서 하는게 맞나?
#! 역시 아니었다. 바로 하나의 알고리즘으로 풀 수 있었다. 

column_temp = 0
row_temp = 0

D_matrix = [[0] * n] * n  #구간합 데이터를 담은 배열 
for i in range(n):
    column_temp += A_matrix[0][i]
    D_matrix[0][i] = column_temp

    row_temp += A_matrix[i][0]
    D_matrix[i][0] = row_temp


#1행과 1열을 제외한 나머지 부분 구간 부분합 구하기 
#* 하나의 알고리즘으로 모두 풀 수 있음 
for i in range(1,n):
    for j in range(1,n):
        D_matrix[i][j] = D_matrix[i][j-1] + D_matrix[i-1][j] - D_matrix[i-1][j-1] + A_matrix[i][j]


# #*STEP3 구간 부분합 구하기 ---------------------------------------------------------------------
for i in range(m):
    x1,y1,x2,y2 = list(map(int,input().split()))  #! 여기도 리스트 필요없음. 
    result = D_matrix[x2][y2] - D_matrix[x1-1][y2] - D_matrix[x2][y1-1] + D_matrix[x1-1][y1-1]
