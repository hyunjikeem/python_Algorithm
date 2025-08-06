def solution(dots):
    x_list = [x for x, y in dots]
    y_list = [y for x, y in dots]
    
    width = max(x_list) - min(x_list)
    height = max(y_list) - min(y_list)
    
    return width * height