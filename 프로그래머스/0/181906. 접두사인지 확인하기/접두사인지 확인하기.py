def solution(my_string, is_prefix):
    my_string = [my_string[:i] for i in range(len(my_string)+1)]
    if is_prefix in my_string:
        return 1
    else:
        return 0 