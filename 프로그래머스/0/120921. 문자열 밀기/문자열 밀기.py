def solution(A, B):
    for i in range(len(A)):
        rotated = A[-i:] + A[:-i]
        if rotated == B:
            return i
        
    return -1