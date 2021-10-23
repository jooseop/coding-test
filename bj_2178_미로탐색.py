from collections import deque
def dfs():
    n, m = map(int, input().split())
    board = [list(map(int, input())) for _ in range(n)]
    way = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    step = [[0] * m for _ in range(n)]
    queue = deque()

    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                queue.append((i, j, step))
                board[i][j] = 0
                step[i][j] = 1

            while queue:
                pop = queue.popleft()

                if pop[0] == n - 1 and pop[1] == m - 1:
                    print(step[pop[0]][pop[1]])
                    return

                for w in way:
                    x, y = w[0] + pop[0], w[1] + pop[1]
                    if 0 <= x < n and 0 <= y < m and board[x][y] == 1:
                        queue.append((x, y))
                        step[x][y] = step[pop[0]][pop[1]] + 1
                        board[x][y] = 0


dfs()
