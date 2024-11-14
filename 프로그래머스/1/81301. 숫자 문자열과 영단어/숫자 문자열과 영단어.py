def solution(s):
    digit_alpha = {'zero': '0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    digit = digit_alpha.values()
    empty_list = []
    tmp = ''
    for i in s:
        if i in digit:
            empty_list.append(i)
        else:
            tmp += i
            if tmp in digit_alpha:
                empty_list.append(digit_alpha[tmp])
                tmp = ''
    return int(''.join(empty_list))