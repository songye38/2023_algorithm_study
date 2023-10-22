def solution(id_pw, db):
    result = 'fail'
    for i in range(len(db)):
        if db[i][0]== id_pw[0]:
            if db[i][1] == id_pw[1]:
                result = 'login'
            else:
                result = 'wrong pw'
    
    return result
        