def solution(arr, queries):
    for s,e in queries:
        for i in range(len(arr)):
            if i>=s and i <=e:
                arr[i] +=1
    return arr