def solution(a, b, c):
    answer = 0
    num_list = list(set([a,b,c]))
    if len(num_list) == 3:
        return a + b + c
    elif len(num_list) == 2:
        return (a+b+c) * (a ** 2 + b ** 2 + c ** 2)
    elif len(num_list) == 1:
        return (a+b+c) * (a ** 2 + b ** 2 + c ** 2) * (a ** 3 + b ** 3 + c ** 3)