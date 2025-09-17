def solution(my_string, indices):
    str_list = list(my_string)
    indices = sorted(indices, reverse=True)
    for i in indices:
        str_list.pop(i)
    return ''.join(str_list)