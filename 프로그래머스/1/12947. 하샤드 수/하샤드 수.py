def solution(x):
    num_list = list(str(x))
    sum_rslt = 0
    for i in num_list:
        sum_rslt += int(i)
    if x % sum_rslt == 0:
        return True
    else:
        return False