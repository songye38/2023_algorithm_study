def solution(dots):
    x_min = min(dots[0][0],dots[1][0],dots[2][0],dots[3][0])
    x_max = max(dots[0][0],dots[1][0],dots[2][0],dots[3][0])
    
    y_min = min(dots[0][1],dots[1][1],dots[2][1],dots[3][1])
    y_max = max(dots[0][1],dots[1][1],dots[2][1],dots[3][1])
    
    return abs(x_min-x_max) * abs(y_min-y_max)
    
    