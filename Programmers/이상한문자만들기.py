def solution(s):
    ans = ''
    arr = list(s.split(' '))
    for i in arr:
        for j in range(len(i)):
            if j % 2 == 0:
                ans += i[j].upper()
            else:
                ans += i[j].lower()
        ans += ' '
    return ans[:-1]