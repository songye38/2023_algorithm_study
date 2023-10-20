import copy
def solution(arr):
    pre_arr= copy.deepcopy(arr)
    post_arr = []
    count= 0
    
    for i in range(len(arr)):
        if arr[i]>=50 and arr[i]%2==0:
            arr[i] = arr[i] // 2
        elif arr[i]<50 and arr[i]%2!=0:
            arr[i] = (arr[i]*2)+1
        else:
            arr[i] = arr[i]
    post_arr = copy.deepcopy(arr)
    count +=1
    
    #---------------------------------------------------------------
    
    
    while pre_arr != post_arr:
        for i in range(len(arr)):
            if arr[i]>=50 and arr[i]%2==0:
                arr[i] = arr[i] // 2
            elif arr[i]<50 and arr[i]%2!=0:
                arr[i] = (arr[i]*2)+1
            else:
                arr[i] = arr[i]
        count +=1
        pre_arr = post_arr
        post_arr = copy.deepcopy(arr)
        
    return count-1
            