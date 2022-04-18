def solution(id_list, report, k):
    answer = [0] * len(id_list)
    
    # 중복 값들 제거
    report = set(report)
    report = list(report)
    # print(report)
    
    dic = {} # 신고된 사람: [신고한 사람]
    for id in id_list :
        dic[id] = []
    # print(dic)
    
    # report에 저장된 값 = 신고한사람 : [신고된 사람]
    for i in report:
        stop = i.split() # split을 이용해서 신고한 사람과 신고한 아이디 나누기 (split을 통해서 절반으로 나누어준다)
        # print(stop)
        dic[stop[1]] += [stop[0]] # 나누어준 값을 dic에 추가
    # print(dic)
        
    for key, value in dic.items(): # dic을 for문으로 순회하면서 k명 이상 신고된 사람을 찾는다
        if len(value) >= k:
            for person in value:
                answer[id_list.index(person)] += 1 # 신고한 사람들의 인덱스 값에 맞춰서 answer값을 +1
        # print(answer)
    return answer