'''
number 문자열을 한 번 다 읽었는데도 k가 남은 경우 스택에서 잘라준다
ex) number, k = '1000', 1
'''
from collections import deque
def solution(number, k):
    stack = []
    number = deque(number)
    
    while number and k > 0:
        pop = number.popleft()       
        while stack and stack[-1] < pop and k > 0:
            stack.pop()
            k -= 1
        stack.append(pop)
    number = list(number)

    # number, k = '1000', 1과 같은 경우 처리
    if k > 0:
        stack = stack[:-1]
        
    answer = stack + number

    return ''.join(answer)
