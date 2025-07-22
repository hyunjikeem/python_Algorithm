def solution(sides):
    max_line = max(sides)
    sides.pop(sides.index(max_line))
    if max_line < sum(sides):
        return 1
    else:
        return 2