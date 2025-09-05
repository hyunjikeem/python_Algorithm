def solution(myString):
    answer = ''
    for s in myString:
        if ord('l') > ord(s):
            answer += 'l'
        else:
            answer += s
    return answer