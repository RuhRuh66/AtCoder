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
<<<<<<< HEAD
        now_point = que.popleft()
        temp_count = maze_count[now_point[0], now_point[1]]

        if 0<= x-1 < H and 0<= y < W:
            if maze[x-1][y] == '.':
                if maze_count[x-1][y] == -1:
                    maze_count[x-1][y] = maze_count[x][y] + 1
                    que.append([x-1, y])



=======
        now_x, now_y = que.popleft()
        count = maze_count[now_x][now_y] 
        
        if 0<=now_x -1 < H and 0<= now_y < W:
            if maze[now_x-1][now_y] == '.':
                if maze_count[now_x-1][now_y] == -1:
                    maze_count[now_x-1][now_y] = count + 1
                    que.append([now_x -1, now_y])
        
        if 0<=now_x  < H and 0<= now_y-1 < W:
            if maze[now_x][now_y-1] == '.':
                if maze_count[now_x][now_y-1] == -1:
                    maze_count[now_x][now_y-1] = count + 1
                    que.append([now_x , now_y-1])

        if 0<=now_x +1 < H and 0<= now_y < W:
            if maze[now_x+1][now_y] == '.':
                if maze_count[now_x+1][now_y] == -1:
                    maze_count[now_x+1][now_y] = count + 1
                    que.append([now_x +1, now_y])

        if 0<=now_x  < H and 0<= now_y+1 < W:
            if maze[now_x][now_y+1] == '.':
                if maze_count[now_x][now_y+1] == -1:
                    maze_count[now_x][now_y+1] = count + 1
                    que.append([now_x , now_y+1])
    
    max_num = 0
    for i in range(H):
        max_num = max(max_num, max(maze_count[i]))
    
    return max_num


max_num = 0
for i in range(H):
    for j in range(W):
        if maze[i][j] == '.':
        
            temp_count = explore(i, j)
            max_num = max(temp_count, max_num)
        
print(max_num)
>>>>>>> 9b95183bd682d384226b5d05112a4f03624a84ba
