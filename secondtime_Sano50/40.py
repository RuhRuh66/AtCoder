from math import cos, sin 
import numpy as np

N = int(input())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

a, b = ((x1+x2)/2, (y1+y2)/2)

t = 2*np.pi/N
rot = np.array([[cos(t), -sin(t)], [sin(t), cos(t)]])

v = np.array([x1-a, y1-b])
w = np.dot(rot, v)

ans = w +[a, b]
print(*ans)