def solution(my_strings, parts):
    answer = ''
    for i, my_string in enumerate(my_strings):
        answer += my_string[parts[i][0]:parts[i][1]+1]
        
    return answer