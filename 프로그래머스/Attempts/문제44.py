import math
from collections import deque
def solution(progresses, speeds):
    answer = []
    date_arr = []
    
    for idx,data in enumerate(progresses):
        temp = math.ceil((100-data) /speeds[idx])
        date_arr.append(temp)
        
    date_queue = deque(date_arr)
    print(date_queue)

    for i,data in enumerate(date_queue):
        print(i,data)


solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])
