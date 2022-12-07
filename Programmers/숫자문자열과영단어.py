def solution(s):
    alpha_digit = {'zero': '0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    digit = alpha_digit.values()
    arr = []
    tmp = ''
    for i in s:
        if i in digit:
            arr.append(i)
        else:
            tmp += i
            if tmp in alpha_digit:
                arr.append(alpha_digit[tmp])
                tmp = ''
    return int(''.join(arr))