import sys

N = int(sys.stdin.readline())

result = [int(input()) for _ in range(N)]

current = 1
stack, answer = [], []

for result in result :
    while current <= result :
        stack.append(current)
        answer.append('+')
        current += 1

    if stack[-1] == result :
        answer.append('-')
        stack.pop()
    
    else :
        print('NO')
        exit(0)

print("\n".join(answer))