def solution(my_string):
    Consonant = ['a','e','i','o','u']
    for cons in Consonant:
        my_string = my_string.replace(cons,"")
        
    return my_string