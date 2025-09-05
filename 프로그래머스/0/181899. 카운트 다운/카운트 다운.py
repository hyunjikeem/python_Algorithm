def solution(start_num, end_num):
    return sorted([i for i in range(end_num, start_num+1)], reverse=True)