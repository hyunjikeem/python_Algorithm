def solution(arr, flag):
    X = []
    # flag[i] 가 true면 빈배열 X에 arr[i]를 arr[i] x 2번
    
    for idx, boolean in enumerate(flag):
        times = arr[idx] * 2
        if boolean == True:
            X += str(arr[idx]) * times
        else:
            X = X[:-arr[idx]]
        
    return [int(num) for num in X]