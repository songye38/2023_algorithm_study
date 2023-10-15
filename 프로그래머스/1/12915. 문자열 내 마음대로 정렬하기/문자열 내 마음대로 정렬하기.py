def solution(strings, n):
    strings.sort()
    strings.sort(key=lambda strings : strings[n])
    return strings