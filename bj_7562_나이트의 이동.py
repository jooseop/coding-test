from collections import deque
def bfs():
    l = int(input())
    board = [[0] * l for _ in range(l)]
    check = [[0] * l for _ in range(l)]
    way = [(-2, -1), (-1, -2), (1, -2), (2, -1),(2, 1), (1, 2), (-1, 2), (-2, 1)]

    a, b = map(int, input().split())
    queue = deque()
    queue.append((a, b))
    board[a][b] = 1
    check[a][b] = 0

    dest_x, dest_y = map(int, input().split())

    while queue:
        pop = queue.popleft()

        if pop[0] == dest_x and pop[1] == dest_y:
            return check[dest_x][dest_y]

        for w in way:
            x, y = pop[0] + w[0], pop[1] + w[1]
            if 0 <= x < l and 0 <= y < l and board[x][y] == 0:
                queue.append((x, y))
                board[x][y] = 1
                check[x][y] = check[pop[0]][pop[1]] + 1


n = int(input())
for _ in range(n):
    print(bfs())
