def solution(arr):
    row = 0
    column = column = len(arr[0])
    for i in range(len(arr)):
        row +=1
        
    if row<column: #열이 더 많은 경우
        for i in range(column-row):
            arr.append([0] * column)
        return arr
    elif column < row:
        for i in range(len(arr)):
            arr[i] +=[0] * (row-column)
        return arr
    else:
        return arr