H, W, X, Y = map(int, input().split())

Maze = [ ]
for i in range(H):
    st = str(input())
    Maze.append(list(st))
    
X, Y = X-1, Y-1

cnt = 1
d = 0
#right
while Y+d < W-1:
    d += 1
    if Maze[X][Y+d] == '#':
        break
    else:
        cnt += 1
d = 0
#left
while Y-d > 0:
    d += 1
    if Maze[X][Y-d] == '#':
        break
    else:
        cnt += 1
d = 0
#down
while X+d < H-1:
    d += 1
    if Maze[X+d][Y] == '#':
        break
    else:
        cnt += 1
#up
d = 0
while X-d > 0:
    d += 1
    if Maze[X-d][Y] == '#':
        break
    else:
        cnt += 1


print(cnt)

    

