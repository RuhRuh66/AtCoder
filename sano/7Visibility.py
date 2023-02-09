H, W, X, Y = map(int, input().split())
X -= 1
Y -= 1
origin = [X, Y]
maze = []
for i in range(H):
    temp = list(str(input()))
    maze.append(temp)
    
count = 1

X, Y = origin
while Y-1>=0:
    if maze[X][Y-1] == '#':
        break
    else:
        count += 1
        Y -= 1
        
X, Y = origin
while Y+1<=W-1:
    if maze[X][Y+1] == '#':
        break
    else:
        count += 1
        Y += 1

X, Y = origin
while X-1>=0:
    if maze[X-1][Y] == '#':
        break
    else:
        count += 1
        X -= 1

X, Y = origin
while X+1<=H-1:
    if maze[X+1][Y] == '#':
        break
    else:
        count += 1
        X +=1

print(count)