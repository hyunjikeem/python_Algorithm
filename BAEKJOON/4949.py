while True:
    lines = input()
    if lines == '.' :
        break
    stack = []
    result = 'yes'
    
    for i in lines :
        if i == '(' or i == '[' :
            stack.append(i)
        elif i == ')' :
            if len(stack) != 0 and stack[-1] == '(' :
                stack.pop()
            else :
                result = 'no'
                break
        elif i == ']' :
            if len(stack) != 0 and stack[-1] == '[' :
                stack.pop()
            else :
                result = 'no'
                break
    if len(stack) == 0 :
        print(result)
    else :
        print('no')