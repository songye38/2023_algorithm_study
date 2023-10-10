def solution(a, b):
    if a < b:
        new_list = [i for i in range(a,b+1)]
        return sum(new_list)
    elif a==b:
        return a
    else:
        new_list = [i for i in range(b,a+1)]
        return sum(new_list)