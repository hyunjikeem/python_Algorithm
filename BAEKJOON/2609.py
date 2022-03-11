# import math

N,X = map(int, input().split())


def gcd(N,X) :
    while X > 0 :
        N, X = X, N % X
    return N

def lcm(N,X) :
    result = (N*X) // gcd(N,X)
    return result
    
print(gcd(N,X))
print(lcm(N,X))

# print(math.gcd(N,X))
# print(math.lcm(N,X))