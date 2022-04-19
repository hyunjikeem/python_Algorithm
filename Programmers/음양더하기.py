def solution(absolutes, signs):
    answer = 0
    # signs가 true면 absolutes[i]의 실제 정수가 양수, 아니면 음수
    for i in range(len(absolutes)):
        # true인 경우 answer에 +
        if signs[i] :
            answer += absolutes[i]
            # false인 경우 answer에서 -
        else :
            answer -= absolutes[i]
    
    return answer