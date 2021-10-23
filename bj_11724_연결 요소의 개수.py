from sys import stdin

n, m = map(int, stdin.readline().split())
d = {i : set() for i in range(1, n + 1)}
check = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    d[a].add(b)
    d[b].add(a)

answer = 0
for i in range(1, n + 1):
    if not check[i]:
        stack = [i]
        check[i] = True

        while stack:
            pop = stack.pop()

            for j in d[pop]:
                if not check[j]:
                    stack.append(j)
                    check[j] = True

        answer += 1

print(answer)
