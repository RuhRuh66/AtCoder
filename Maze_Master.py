H, W = map(int, input().split())
maze = []

for i in range(H):
    j = list(input())
    maze.append(j)


def move_count(start_point, end_point):
    
    