def solution(numbers):
    answer = 0
    # numbers의 길이가 1 <= numbers의 길이 <= 10 이기 때문에 range(10)으로 반복
    for i in range(10):
        # i가 numbers 안에 없다면
        if i not in numbers:
            # answer에 + i 해주면서 계속 없는 숫자를 찾는다
            answer += i
    return answer