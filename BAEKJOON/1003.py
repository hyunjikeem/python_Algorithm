f0 = [1, 0, 1]
f1 = [0, 1, 1]

def fibonacci(N) :
    length = len(f0)
    if length <= N :
        for i in range(length, N+1) :
            f0.append(f0[i-1] + f0[i-2])
            f1.append(f1[i-1] + f1[i-2])
    print(f0[N], f1[N])
    
T = int(input())

for _ in range(T) :
    fibonacci(int(input()))

