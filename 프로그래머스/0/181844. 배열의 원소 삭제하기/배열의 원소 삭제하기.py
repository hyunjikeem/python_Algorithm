def solution(arr, delete_list):
    duplicate_num = list(set(arr)&set(delete_list))
    if duplicate_num:
        for num in duplicate_num:
            arr.remove(num)
    return arr