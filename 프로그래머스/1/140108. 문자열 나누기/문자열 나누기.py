def solution(s):
    print(s)
    first_word = ''
    idx = same = not_same = 0
    for i in s:
        if same == not_same:
            first = i
            idx += 1
        if i == first:
            same += 1
        else:
            not_same += 1
    return idx