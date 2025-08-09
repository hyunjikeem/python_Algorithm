import sys
N = int(sys.stdin.readline())
nums = list(map(int, input().split()))

max_score = max(nums)

score_list = []
for i in nums:
    score_list.append(i/max_score*100)
    
print(sum(score_list)/N)