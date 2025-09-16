def solution(arr):
    X = []
    for i in arr:
        X += [i] * i
    return X