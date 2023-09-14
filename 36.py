answer =  0
A = list(map,str,input().split('-'))


def mySum(data):
    sum = 0
    result = data.split("+")
    for i in range(len(result)):
        sum += int(result[i])
    return sum

for i in range(len(A)):
    temp = mySum(A[i])
    if i==0:
        answer += temp
    else:
        answer -= temp


print(answer)

