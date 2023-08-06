#
#선택 정렬의 핵심
data = [42,32,24,60,15]
min = 10000

for j in range(len(data)):
    min_index = j # 0
#최소값 찾기 과정
    for i in range(j,len(data)):
        if data[i] < min:
            min = data[i]
            min_index = i

    temp = data[j]
    data[j] = data[min_index]
    data[min_index] = temp
    print(j,"번째 데이터 sorting")
    print(data)
    print("------------------------------")



    




#A = list(input())

#for i in range(len(A)):
