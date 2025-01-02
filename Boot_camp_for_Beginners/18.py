sx, sy, tx, ty = map(int, input().split())

dx = tx-sx
dy = ty-sy

forth_1 = 'R' * dx + 'U' * dy
back_1 = 'L' * dx + 'D' * dy
forth_2 = 'D' + 'R' * (dx+1) + 'U' * (dy+1) + 'L'
back_2 = 'U' + 'L' * (dx+1)  + 'D' * (dy+1) + 'R'

print(forth_1+back_1+forth_2+back_2)

