def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        arr_sum = []
        for j in range(len(arr1[0])):
            # 각각의 요소들을 더해준다
            arr_sum.append(arr1[i][j] + arr2[i][j])
        # print(arr_sum)
        # 리스트에 append
        answer.append(arr_sum)
    return answer