N, K = map(int, input().split())

coin = []
count = 0

for i in range(N):
    coin.insert(0, int(input()))

for i in coin:
    count += K // i
    K = K % i

print(count)