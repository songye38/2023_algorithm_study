checkList =[0] * 4 
myList = [0] * 4
checkSecret = 0

def myadd(c):
    global checkList, myList,checkSecret
    if c =='A':
        myList[0] +=1
        if myList[0] == checkList[0]:
            checkSecret +=1
                                                                                                                                                                                                                              
def myremove(c):
    pass


S = int(input()) #전체 문자열 크기
P = int(input()) #부분 문자열 길이
A = input()

checkList = input()



