N, K = map(int, input().split())
list = []
cnt = 0

for i in range(N) :
    list.insert(0, int(input()))

for i in list :
    cnt += K // i
    K %= i
    if K == 0 :
        break

print(cnt)