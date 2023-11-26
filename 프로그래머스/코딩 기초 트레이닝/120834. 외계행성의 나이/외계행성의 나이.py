import string
def solution(age):
    age_dict = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9}
    answer = ""
    age = list(str(age))
    for i in age:
        i = int(i)
        answer += list(age_dict.keys())[list(age_dict.values()).index(i)]
    return answer