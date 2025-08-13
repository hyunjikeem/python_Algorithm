N = int(input())
meetings = []
for _ in range(N):
    I, J = map(int, input().split())
    meetings.append((I, J))

meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
last_end = 0
for i, j in meetings:
    if i >= last_end:
        count += 1
        last_end = j

print(count)