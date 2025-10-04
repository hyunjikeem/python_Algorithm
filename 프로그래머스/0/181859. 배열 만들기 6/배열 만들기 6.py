def solution(arr):
    stk = []
    idx = 0
    for i in arr:
        if not stk:
            stk.append(i)
        else:
            if stk[-1] == i:
                stk.pop()
            else:
                stk.append(i)
    return stk if stk else [-1]