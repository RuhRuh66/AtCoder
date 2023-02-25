N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

C = [(A[0]+B[0])/2, (A[1]+B[1])/2]

import math

rad = math.pi*2/N

moved_A_x = A[0]-C[0]
moved_A_y = A[1]-C[1]

rotate_x = moved_A_x * math.cos(rad) - moved_A_y*math.sin(rad)
rotate_y = moved_A_x * math.sin(rad) + moved_A_y*math.cos(rad)

ans_x = rotate_x+C[0]
ans_y = rotate_y+C[1]

print(ans_x, ans_y)