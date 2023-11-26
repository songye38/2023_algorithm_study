def solution(myString, pat):
    count = 0
    answer = [myString[i:i+len(pat)] for i in range(len(myString)-len(pat)+1)]
    for part_string in answer:
        if pat ==part_string:
            count +=1
    return count