def function(arg):
    stack = []
    for i in arg:
        if stack:
            if i == ')' and stack[-1] == '(':
                stack.pop()
                continue
        stack.append(i)

    if stack:
        return "NO"
    return "YES"


n = int(input())
for _ in range(n):
    s = input()
    print(function(s))
