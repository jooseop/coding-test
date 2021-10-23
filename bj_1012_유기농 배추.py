import sys
for _ in range(int(input())):
    m, n, k = map(int, sys.stdin.readline().split())
    board = [[0] * m for _ in range(n)]

    for _ in range(k):
        a, b = map(int, sys.stdin.readline().split())
        board[b][a] = 1

    way = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    stack = []
    answer = 0

    for x in range(n):
        for y in range(m):
            if board[x][y] == 1:
                stack.append((x, y))
                answer += 1

            while stack:
                pop = stack.pop()
                if 0 <= pop[0] < n and 0 <= pop[1] < m and board[pop[0]][pop[1]] == 1:
                    board[pop[0]][pop[1]] = 0
                    
                    for w in way:
                        wx, wy = pop[0] + w[0], pop[1] + w[1]
                        stack.append((wx, wy))

    print(answer)
