'''
받아온 n을 str으로 변환해서 list 형태로 만들어준다
reverse()를 사용해 list형태로 만들어둔 n을 뒤집어준다
문자열을 정수로 리턴해야하기 때문에 map을 사용해 준다
'''
def solution(n):
    list_n = list(str(n))
    list_n.reverse()
    return list(map(int, list_n))