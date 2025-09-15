def solution(myString):
    string = myString.split('x')
    return [len(s) for s in string]