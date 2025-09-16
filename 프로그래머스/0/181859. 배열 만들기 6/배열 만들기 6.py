def solution(arr):
    # arr 를 이용해 새로운 배열 stk 만듦
    # i의 초기값 0, i가 arr의 길이보다 작으면 다음을 반복
    # stk이 빈배열이라면 -> arr[i]를 stk에 추가, i += 1
    # stk에 원소가 있고 stk의 마지막 원소가 arr[i]와 같으면 stk의 마지막 원소를 stk에서 제거, i += 1
    # stk에 원소가 있고 stk의 마지막 원소가 arr[i]와 다르면 stk의 맨 마지막에 arr[i] 추가, i += 1
    stk = []
    for idx in arr:
        if len(stk) == 0:
            stk.append(idx)
        else:
            if stk[-1] == idx:
                stk.pop()
            else:
                stk.append(idx)
    if not stk:
        return [-1]
    return stk