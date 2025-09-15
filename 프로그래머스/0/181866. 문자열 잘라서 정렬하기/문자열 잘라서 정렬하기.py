def solution(myString):
    string = myString.split('x')
    filtered_string = [s for s in string if s]
    return sorted(filtered_string)