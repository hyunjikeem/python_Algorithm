t = int(input())

for i in range(t) :
    x, y = map(int, input().split())
    distance = y - x
    n = 1
    
    while True :
        if n ** 2 <= distance < (n + 1) ** 2 :
            break
        else :
            n += 1
    
    if n ** 2 == distance :
        print((n * 2) -1)
    elif n ** 2 < distance <= n ** 2 + n :
        print(n * 2)
    else :
        print((n * 2) + 1)