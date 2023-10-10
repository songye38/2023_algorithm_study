# #sudo

# n = int(input())
# A = [0] * n
# for i in range(n):
#     A[i] = int(input())



# before_sort_index = {} #정렬 전 인덱스
# after_sort_index = [i for i in range(n)]


# for i in range(n):
#     before_sort_index[str(A[i])] = i

# A.sort()

# max = 0
# for i in range(n):
#     result = before_sort_index[str(A[i])] - after_sort_index[i]
#     if max < result :
#         max = result


# print("_------------------------------")
# print(max+1)


#answer

import sys
input = sys.stdin.readline

N = int(input())
A = []

for i in range(N):
    A.append((int(input()),i))

Max = 0
sorted_A = sorted(A)

for i in range(N):
    if Max < sorted_A[i][1] - i:
        Max = sorted_A[i][1] - i

print(Max+1)
