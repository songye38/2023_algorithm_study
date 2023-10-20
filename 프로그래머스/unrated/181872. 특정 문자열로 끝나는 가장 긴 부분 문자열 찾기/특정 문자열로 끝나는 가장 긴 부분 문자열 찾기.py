def solution(myString, pat):
    end_index = len(pat)
    start_index = myString.rfind(pat) 
    return myString[:start_index+ end_index]