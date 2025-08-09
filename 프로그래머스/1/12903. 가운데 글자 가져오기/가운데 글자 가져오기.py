def solution(s):
    s_list = list(s)
    answer = []
    if len(s) % 2 != 0:
        answer.append(s_list[len(s) // 2])
    else:
        answer.append(s_list[len(s) // 2 -1])
        answer.append(s_list[len(s) // 2])
    
    return ''.join(answer)