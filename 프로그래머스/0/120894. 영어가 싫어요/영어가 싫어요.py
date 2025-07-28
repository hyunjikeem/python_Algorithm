def solution(numbers):
    num_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'zero': '0'}
    for word, digit in num_dict.items():
        numbers = numbers.replace(word, digit)
    
    return int(numbers)