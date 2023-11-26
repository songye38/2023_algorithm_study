def solution(myString):
    myString = list(myString)
    for i in range(len(myString)):
        if myString[i] == 'a':
            myString[i] = 'A'
        elif myString[i]!='a' and myString[i].islower():
            continue
        elif myString[i]!='A' and myString[i].isupper():
            myString[i] = myString[i].lower()
    return "".join(myString)