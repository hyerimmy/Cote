def solution(id_pw, db):
    answer = 'fail'

    for i in range(0,len(db)):
        if id_pw[0] == db[i][0]:
            if id_pw[1] == db[i][1]:
                return "login"
            else:
                return "wrong pw"

    return answer