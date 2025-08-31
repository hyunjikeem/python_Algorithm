def solution(name, yearning, photo):
    # 점수 dict key: name value: yearning
    score_dict = {}
    result = [0] * len(photo)
    for idx, n in enumerate(name):
        score_dict[n] = yearning[idx]
    
    for idx, p in enumerate(photo):
        for n in p:
            if n in score_dict:
                result[idx] += score_dict[n]
            else:
                result[idx] += 0
    return result