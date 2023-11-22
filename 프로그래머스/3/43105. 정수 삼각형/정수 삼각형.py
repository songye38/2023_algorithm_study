import sys
sys.setrecursionlimit(10**6)


def getValResult(pre_arr,post_arr):
    answer = [0] * len(post_arr)
    answer[0] = post_arr[0] + pre_arr[0]
    answer[-1] = post_arr[-1] + pre_arr[-1]
    for i in range(1,len(post_arr)-1):
        max = post_arr[i] + pre_arr[i-1]
        if max < post_arr[i] + pre_arr[i]:
            max = post_arr[i] + pre_arr[i]
        answer[i] = max
    return answer

    
def getMaxTriangleVal(val_arr,triangle):
    if len(triangle)==2:
        val_arr = [int(triangle[0][0])+int(triangle[1][0]),int(triangle[0][0])+int(triangle[1][1])]
        return val_arr
    else:
        val_arr = getMaxTriangleVal(val_arr,triangle[:-1])
        val_arr = getValResult(val_arr,triangle[-1])
        return val_arr

def solution(triangle):
    val_arr = []
    result = getMaxTriangleVal(val_arr,triangle)
    print(max(result))
    return max(result)
        
        