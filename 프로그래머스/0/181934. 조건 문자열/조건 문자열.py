def solution(ineq, eq, n, m):
    if eq == '!':
        if ineq == '<':
            return (n < m) *1
        else:
            return (n > m) *1
    else:
        if ineq == '<':
            return (n <= m) *1
        else:
            return (n >= m) *1