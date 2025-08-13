def solution(n, lost, reserve):
    # 학생들의 번호는 체격 순으로 매겨져 있음
    # 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있음
    # 예를들어, 4번 학생은 3번 학생이나 5번 학생에게만 빌려줄 수 있음
    
    # 전체학생수: n, 체육복을 도난당한 학생들의 번호가 담긴 배열: lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열: reserve
    
    lost = set(lost)
    reserve = set(reserve)
    
    # 겹치는 학생 제거
    overlap = lost & reserve
    lost -= overlap
    reserve -= overlap
    
    # 여벌로 빌려주기
    for r in sorted(reserve):
        if r - 1 in lost:
            lost.remove(r - 1)
        elif r + 1 in lost:
            lost.remove(r + 1)
            
    return n - len(lost)