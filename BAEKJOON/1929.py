import math

# def is_prime(n) :
#     if n == 2 :
#         return True

#     if n % 2 == 0 :
#         return False
    
#     for i in range(2, int(math.sqrt(n)) + 1) :
#         if n % i == 0 :
#             return False

#     return True

def is_prime(n) :
    i = 2

    if n <= 1 :
        return False
    
    while i <= n / i :
        if n % i == 0 :
            return False
        i += 1
    return True

m, n = map(int, input().split())

for i in range (m, n + 1) :
    if is_prime(i):
        print(i)