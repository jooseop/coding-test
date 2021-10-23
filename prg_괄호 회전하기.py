def test(s):
    s, stack = list(s), []
    while s:
        p = s.pop()
        
        if stack and ((stack[-1] == '}' and p == '{') or (stack[-1] == ']' and p == '[') or (stack[-1] == ')' and p == '(')):
            stack.pop()
        else:
            stack.append(p)

    return 1 if len(stack) == 0 else 0
            

def solution(s):
    answer = 0
    for i in range(len(s)):
        s = s[1:] + s[0]
        answer += test(s)
    return answer
