n = nbr = int(input())
cnt = 0

while True :
    sum = n // 10 + n % 10
    new_nbr = n % 10 * 10 + sum % 10
    cnt += 1

    n = new_nbr

    if new_nbr == nbr :
        break

print (cnt)