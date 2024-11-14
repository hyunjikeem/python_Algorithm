def solution(nums):
    set_num_len = len(set(nums))
    nums_len = int(len(nums)/2)
    if set_num_len > nums_len:
        answer = nums_len
    else:
        answer = set_num_len
    return answer