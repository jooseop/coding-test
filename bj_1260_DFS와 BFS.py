'''
1. 순회(for), 2. 검증&체크(if)

dfs : pop + if&check -> for
bfs : popleft -> for + if&check
'''
from collections import deque

def dfs(v):
    stack = [v]
    check = [0] * (n + 1)
    answer = []

    while stack:
        pop = stack.pop()
        if check[pop] != 1:
            check[pop] = 1
            answer.append(pop)
            for i in sorted(adj[pop], reverse=True):
                stack.append(i)

    print(' '.join(map(str, answer)))

def bfs(v):
    queue = deque()
    queue.append(v)
    check = [0] * (n + 1)
    check[v] = 1
    answer = []

    while queue:
        pop = queue.popleft()
        answer.append(pop)
        for i in sorted(adj[pop]):
            if check[i] != 1:
                queue.append(i)
                check[i] = 1

    print(' '.join(map(str, answer)))


n, m, v = map(int, input().split())
adj = {i:[] for i in range(1, n + 1)}

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
# print(adj)
dfs(v)
bfs(v)
