def solution(s):
    stack = []
    for i in s:
        if i not in stack:
            stack.append(i)
        else:
            if i  == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
    if stack:
        return 0
    else:
        return 1