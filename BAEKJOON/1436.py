N = int(input())

cnt = 0
nbr = 666

while True :
    if "666" in str(nbr) :
        cnt += 1
    if cnt == N :
        print(nbr)
        break

    nbr += 1