def solution(my_string, n):
    arr = []
    for i in range(len(my_string)):
        for j in range(n):
            arr.append(my_string[i])
    return ''.join(arr)