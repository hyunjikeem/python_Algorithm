N = int(input())
time = list(map(int, input().split()))
time.sort()

result = 0

for i in range(1, N) :
    time[i] += time[i-1]

print(sum(time))