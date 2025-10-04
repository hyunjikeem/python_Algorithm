def solution(my_string, overwrite_string, s):
    str_length = len(overwrite_string)
    answer = my_string[:s] + overwrite_string + my_string[s+str_length:]
    return answer