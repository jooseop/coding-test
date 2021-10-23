# 순열
def function1():
    if len(check) == m:
        print(' '.join(map(str, check)))
        return

    for i in range(1, n + 1):
        if i not in check:
            check.append(i)
            function()
            check.pop()
            
# 조합
def function2(k):
    if len(check) == m:
        print(' '.join(map(str, check)))
        return

    for i in range(k, n + 1):
        if i not in check:
            check.append(i)
            function(i)
            check.pop()

# 중복순열
def function3():
    if len(check) == m:
        print(' '.join(map(str, check)))
        return

    for i in range(1, n + 1):
        check.append(i)
        function()
        check.pop()

# 중복조합
def function(k):
    if len(check) == m:
        print(' '.join(map(str, check)))
        return

    for i in range(k, n + 1):
        check.append(i)
        function(i)
        check.pop()


