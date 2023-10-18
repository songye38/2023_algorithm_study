def solution(array):
    val_list = [0] * 10
    for i in array:
        for num in str(i):
            val_list[int(num)] += 1
    return val_list[7]