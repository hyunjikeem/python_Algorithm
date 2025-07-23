from collections import deque
def solution(numbers, direction):
    arr = deque(numbers)
    if direction == 'right':
        arr.rotate(1)
        return list(arr)
    else:
        arr.rotate(-1)
        return list(arr)