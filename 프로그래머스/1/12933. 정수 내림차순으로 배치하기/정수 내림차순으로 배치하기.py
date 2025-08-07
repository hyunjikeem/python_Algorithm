def solution(n):
    n_list = sorted([int(i) for i in str(n)], reverse=True)
    
    return int(''.join(map(str, n_list)))