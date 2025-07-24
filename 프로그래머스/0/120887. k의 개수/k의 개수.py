def solution(i, j, k):
    answer = 0
    tmp_list = []
    for n in range(i, j+1):
        tmp_list.append(str(n))
    
    return sum(s.count(str(k)) for s in tmp_list)
    