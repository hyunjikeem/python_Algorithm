def solution(id_pw, db):
    id, pw = id_pw
    print(pw)
    for db_id, db_pw in db:
        if id == db_id:
            if pw == db_pw:
                return 'login'
            else:
                return 'wrong pw'
    return 'fail'
