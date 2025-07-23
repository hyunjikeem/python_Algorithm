def solution(my_string, letter):
    for s in my_string:
        if s == letter:
            my_string = my_string.replace(letter, '')
            
    return my_string