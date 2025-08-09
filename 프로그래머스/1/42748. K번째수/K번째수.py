def solution(array, commands):
    answer = []
    for i,j,k in commands:
        pick_nums = array[i-1:j]
        answer.append(sorted(pick_nums)[k-1])
    return answer