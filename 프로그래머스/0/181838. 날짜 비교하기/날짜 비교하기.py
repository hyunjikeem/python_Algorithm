def solution(date1, date2):
    if date1 == date2:
        return 0
    y1, m1, d1 = date1
    y2, m2, d2 = date2
    if y1 < y2:
        return 1
    elif y1 > y2:
        return 0
    
    if m1 < m2:
        return 1
    elif m1 > m2:
        return 0
    
    if d1 < d2:
        return 1
    elif d1 > d2:
        return 0