def solution(num, k):
    if str(k) in str(num):
        index = str(num).index(str(k))
        return int(index) + 1
    else:
        return -1