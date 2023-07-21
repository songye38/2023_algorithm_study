
##**************************************************************
#* 23.07.21(수)
#* step1 입력받고 원본 배열 만들기
#* step2 부분합 배열 만들기 & 변경된 부분합 배열 만들기
#* step3 구간의 개수 출력하기 
#**************************************************************


# refactoring한 결과 ------------------------------------------
import sys
from itertools import combinations

n, m = map(int,input().split())
A = list(map(int,input().split()))


S = []
temp = 0
for i in A:
    temp += i
    S.append(temp)

S_ = [i%m for i in S] ##[1, 0, 0, 1, 0]
 

result = 0
for i in range(m): #많으면 102 
    result += len(list(combinations([k for k in S_ if k==i],2)))

result += S_.count(0)
print(result)