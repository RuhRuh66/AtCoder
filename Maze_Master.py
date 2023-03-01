H, W = map(int, input().split())
maze = []

for i in range(H):
    temp = list(input())
    maze.append(temp)

from collections import deque

def explore(x, y):
    maze_count = [[-1] * W for _ in range(H)]
    que = deque()

    maze_count[x][y] = 0
    que.append([x, y])

    while len(que) > 0:
        now_point = que.popleft()
        temp_count = maze_count[now_point[0], now_point[1]]

        if 0<= x-1 < H and 0<= y < W:
            if maze[x-1][y] == '.':
                if maze_count[x-1][y] == -1:
                    maze_count[x-1][y] = maze_count[x][y] + 1
                    que.append([x-1, y])



