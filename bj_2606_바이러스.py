n = int(input())
m = int(input())
check = []
adj = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

stack = [1]

while stack:
    pop = stack.pop()
    if pop not in check:
        check.append(pop)

        for i in adj[pop]:
            if i not in stack:
                stack.append(i)

print(len(check) - 1)
