def solution(num, total):
    offset = (num * (num -1)) // 2
    x = (total - offset) // num
    
    return [x + i for i in range(num)]