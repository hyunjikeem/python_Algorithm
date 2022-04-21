def solution(x, n):
    answer = []
    # for 문으로 n+1만큼 반복
    for i in range(1, n + 1):
        # answer에 x * i append해주기
        answer.append(x * i)
    # print(answer)
    return answer