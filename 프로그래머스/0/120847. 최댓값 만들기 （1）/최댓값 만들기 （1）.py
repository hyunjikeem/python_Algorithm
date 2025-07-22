def solution(numbers):
    max_list = sorted(numbers, reverse=True)[:2]
    return max_list[0] * max_list[1]