'''
my_string을 list로 만들어주고 for문으로 루프를 돌면서 i와 letter가 같지 않을때, 빈 배열인 arr2에 하나씩 append 해준다
join을 해용해서 arr2에 모인 알파벳들을 하나의 단어로 합쳐줌
'''
def solution(my_string, letter):
    arr = list(my_string)
    arr2 = []
    print(arr)
    for i in arr:
        if not i == letter:
            arr2.append(i)
    return ''.join(arr2)