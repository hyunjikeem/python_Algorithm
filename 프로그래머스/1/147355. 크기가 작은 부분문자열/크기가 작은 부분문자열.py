def solution(t, p):
    p_len = len(p)
    t_arr_by_p_len = [t[i:i+p_len] for i in range(len(t) - len(p) +1)]
    answer = 0
    for i in t_arr_by_p_len:
        if int(p) >= int(i):
            answer += 1
    return answer