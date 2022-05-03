import datetime

def solution(a, b):
    date = 'MON TUE WED THU FRI SAT SUN'.split()
    return date[datetime.date(2016, a, b).weekday()]

# datetime의 내장모듈의 date 클래스는 날짜를 표현하는데 사용됨
# date 클래스의 생성자는 연,월,일 데이터를 인자로 받음
# date 클래스의 weekday() 메서드는 해당 날짜가 무슨 요일인지를 파악하기 위해 사용됨
# weekday()은 월요일이 0으로 시작함