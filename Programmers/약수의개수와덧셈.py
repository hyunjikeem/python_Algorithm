def solution(left, right):
    num = 0
    for i in range(left, right+1):
        add_num = 0
        for j in range(1, i+1):
            if i % j == 0:
                add_num += 1
        if add_num % 2 == 0:
            num += i
        else:
            num -= i
    return num