def solution(s):
    answer = ''
    
    # 단어의 갯수가 홀수일 때
    if (len(s) % 2 == 1):
        # s의리스트 s[]를 만든다음 해당 인덱스의 값을 출력하기 위해 len(s) // 2 를 한 인덱스의 값을 반환한다
        answer = s[len(s) // 2]
        # 짝수일 때
    else:
        # 짝수에서 출력하는 인덱스의 len(s) // 2 - 1 값과 len(s) // 2 값을 같이 반환한다
        answer = s[len(s) // 2 - 1] + s[len(s) // 2]
    return answer