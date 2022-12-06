def solution(n):
    num = []
    for i in range(1, n):
        if n % i == 1:
            num.append(i)
    return num[0]