def solution(n):
    answer = []
    for i in range(1, n+1):
        if n % i == 0:
            j = n // i
            answer.append((i,j))
            if i != j:
                answer.append((j,i))
    return len(set(answer))