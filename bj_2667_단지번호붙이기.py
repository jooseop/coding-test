from collections import deque

n = int(input())
board = [list(map(int, input())) for _ in range(n)]
way = [(0, 1), (0, -1), (1, 0), (-1, 0)]
queue = deque()
answer = []
count = 0
for i in range(n):
    for j in range(n):

        if board[i][j] == 1:
            queue.append((i, j))
            board[i][j] = 0
            count = 1

        while queue:
            pop = queue.popleft()

            for w in way:
                x = pop[0] + w[0]
                y = pop[1] + w[1]
                if 0 <= x < n and 0 <= y < n and board[x][y] == 1:
                    board[x][y] = 0
                    queue.append((x, y))
                    count += 1
        if count != 0:
            answer.append(count)
            count = 0
print(len(answer))
for c in sorted(answer):
    print(c)
