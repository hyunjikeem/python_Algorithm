from collections import Counter

def solution(array):
    count = Counter(array)
    most_common = count.most_common()

    # 최빈값의 빈도 비교
    if len(most_common) == 1 or most_common[0][1] > most_common[1][1]:
        return most_common[0][0]  # 유일한 최빈값
    else:
        return -1  # 여러 개 있음
