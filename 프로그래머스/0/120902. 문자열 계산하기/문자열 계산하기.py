import re
def solution(my_string):
    my_str = my_string.replace(' ', '')
    operators = [s for s in my_str if not s.isdigit()]
    nums = re.findall(r'\d+', my_string)
    numbers = [int(i) for i in nums]
    answer = numbers[0]
    numbers.remove(answer)
    while operators:
        operator = operators[0]
        operators.remove(operator)
        number = numbers[0]
        numbers.remove(number)
        if operator == '+':
            answer += number
        if operator == '-':
            answer -= number
    return answer