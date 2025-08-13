N, K = map(int, input().split())

coin = []
cnt = 0

for i in range(N) :
    coin.insert(0, int(input()))

for i in coin :
    cnt += K // i
    K = K % i

print(cnt)