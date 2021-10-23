def solution(n, computers):
    answer = 0
    check = [False] * n
    d = {idx : [] for idx in range(n)}
    for idx, computer in enumerate(computers):
        for i, c in enumerate(computer):
            if idx == i:
                continue
            if c == 1:
                d[idx].append(i)
                
    for i in range(n):
        if not check[i]:
            check[i] = True
            stack = [i]
            
            while stack:
                pop = stack.pop()
                for j in d[pop]:
                    if not check[j]:
                        check[j] = True
                        stack.append(j)
            answer += 1
            
    return answer
