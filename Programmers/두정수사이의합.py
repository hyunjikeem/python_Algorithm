def solution(a, b):
    # range()를 사용하면 a = 3, b = 5일 경우 3 + 4만 return 하기 때문에 3,4,5를 더해주기 위해 + 1해준다
    if a < b:
        return sum(list(range(a, b + 1)))
    else :
        return sum(list(range(b, a + 1)))