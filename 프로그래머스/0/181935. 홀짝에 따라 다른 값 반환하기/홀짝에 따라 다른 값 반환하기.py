def solution(n):
    arr = []
    if n % 2 == 0:
        arr = [i * i for i in range(1, n+1) if i % 2 == 0]
        return sum(arr)
    else:
        arr = [i for i in range(1, n+1) if i % 2 != 0]
        return sum(arr)