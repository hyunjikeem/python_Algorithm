def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if len(answer) < 1:
        answer.append(-1)
    answer = sorted(answer)
    return answer

# sorted() 함수 = 첫 번째 매개변수로 들어온 iterable한 데이터를 새로운 정렬된 리스트로 만들어서 반환해 주는 함수
# sorted(정렬할 데이터)
# 리스트.sort() 와 sorted(리스트)와 가장 큰 차이
# 리스트.sort()는 본체의 리스트를 정렬해서 변환
# sorted(리스트)는 본체 리스트는 내버려두고, 정렬한 새로운 리스트를 반환