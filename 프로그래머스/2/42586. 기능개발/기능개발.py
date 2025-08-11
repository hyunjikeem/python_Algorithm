def solution(progresses, speeds):
    # 작업의 개수는 100개 이하
    # 작업 진도 progresses  는 100 미만의 자연수
    # 작업 속도 speeds 는 100 이하의 자연수
    # 배포는 하루에 한 번만 할 수 있음. 하루의 끝에 이루어진다고 가정.
    # 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일뒤에 이루어짐.
    days = []
    answer = []
    for i,j in enumerate(progresses):
        if (100 - j) % speeds[i] != 0:
            day = (100 - j) // speeds[i] + 1 
        else:
            day = (100 - j) // speeds[i]
        days.append(day)
    
    current = days[0]
    release = 1
    for day in days[1:]:
        # print('current', current)
        # print('day', day)
        if day <= current:
            release += 1
        else:
            answer.append(release)
            current = day
            release = 1
    answer.append(release)
    return answer