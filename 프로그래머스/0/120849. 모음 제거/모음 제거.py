def solution(my_string):
    vowels = ['a', 'i','o','e','u']
    return ''.join([vow for vow in my_string if vow not in vowels])