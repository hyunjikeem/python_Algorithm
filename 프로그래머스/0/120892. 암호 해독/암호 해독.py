def solution(cipher, code):
    answer = ''
    for idx, s in enumerate(cipher):
        num = idx+1
        if num % code == 0:
            answer += s
            
    return answer