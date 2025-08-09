N = int(input())  # 첫 줄: 수의 개수 N
numbers = [int(input()) for _ in range(N)]  # 다음 N줄: 수

sorted_nums = sorted(numbers)

for i in sorted_nums:
    print(i)