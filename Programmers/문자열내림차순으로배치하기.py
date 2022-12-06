'''
받은 s를 리스트에 넣어주고 sort로 정렬, reverse로 순서를 뒤집어준다
join을 이용해 하나의 문자로 만들어준다
'''
def solution(s):
    s = list(s)
    s.sort(reverse=True)
    return ''.join(s)