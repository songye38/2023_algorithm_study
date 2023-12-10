def solution(numbers, hand):
    answer = ""
    pos = [[3,1],[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2],[3,0],[3,2]]
    left = 10
    right = 11
    for idx,num in enumerate(numbers):
        if num in [1,4,7]:
            left = num
            answer += 'L'
        elif num in [3,6,9]:
            right = num
            answer += 'R'
        else:
            left_gap = abs(pos[left][0] - pos[num][0])+abs(pos[left][1] - pos[num][1])
            right_gap = abs(pos[right][0] - pos[num][0])+abs(pos[right][1] - pos[num][1])
            if left_gap < right_gap:
                left = num
                answer += 'L'
            elif left_gap > right_gap:
                right = num
                answer += 'R'
            else:
                if hand=='right':
                    right = num
                    answer += 'R'
                else:
                    left = num
                    answer += 'L'
                
    
    return answer