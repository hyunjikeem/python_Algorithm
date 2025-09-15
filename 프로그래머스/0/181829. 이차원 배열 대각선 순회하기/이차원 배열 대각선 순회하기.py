def solution(board, k):
    n, m = len(board), len(board[0])
    total = 0
    for i in range(min(n, k+1)):
        max_j = min(m-1, k-i)
        for j in range(max_j + 1):
            total += board[i][j]
    return total