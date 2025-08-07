def solution(n):
    i = 1
    fact = 1
    while True:
        fact *= i
        if fact > n:
            return i - 1
        
        i += 1