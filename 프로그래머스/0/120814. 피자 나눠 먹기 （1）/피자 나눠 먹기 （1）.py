def solution(n):
    if n % 7 > 0:
        return int(n/7)+1
    else:
        return n // 7