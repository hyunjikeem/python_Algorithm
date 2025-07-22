def solution(money):
    answer = []
    coffee = money // 5500
    return [coffee, money - (coffee * 5500)]