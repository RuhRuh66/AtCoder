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
        
    