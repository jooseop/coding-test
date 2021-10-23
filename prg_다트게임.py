import re
def solution(dartResult):
    stack = []

    for num, char in zip(re.findall('[1][0]|[0-9]', dartResult), re.split('[1][0]|[0-9]', dartResult)[1:]):
        if char[0] == 'S':
            stack.append(int(num) ** 1)
        elif char[0] == 'D':
            stack.append(int(num) ** 2)
        elif char[0] == 'T':
            stack.append(int(num) ** 3)
        
        if len(char) == 2:
            if char[1] == '*':
                prev = stack.pop() * 2
                if stack:
                    prevprev = stack.pop() * 2
                    stack.append(prevprev)
                stack.append(prev)
            
            else:
                prev = stack.pop() * -1
                stack.append(prev)
    
    return sum(stack)
