def solution(myString, pat):
    temp_list = [0 if i=='A' else 1 for i in list(myString)]
    answer = "".join(['B' if i==0 else 'A' for i in temp_list])
    if pat in answer:
        return 1
    else:
        return 0