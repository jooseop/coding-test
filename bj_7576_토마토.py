from collections import deque
def bfs():
    m, n = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    way = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # bfs
    queue = deque()
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                queue.append((i, j))
    while queue:
        pop = queue.popleft()
        for w in way:
            x, y = pop[0] + w[0], pop[1] + w[1]
            if 0 <= x < n and 0 <= y < m and board[x][y] == 0:
                board[x][y] = board[pop[0]][pop[1]] + 1
                queue.append((x, y))

    max_board = 0
    for b in board:
        if 0 in b:
            return -1
        max_board = max(max_board, max(b))
    else:
        return max_board - 1


print(bfs())
