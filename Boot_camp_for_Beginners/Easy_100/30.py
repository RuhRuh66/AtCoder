x1, y1, x2, y2 = map(int, input().split())

a = (x1+y1+x2-y2)/2
b = (x2+y2-x1+y1)/2

x3 = -y2+b+a
y3 = x2-a+b

x4 = -y3+b+a
y4 = x3-a+b

print(int(x3), int(y3), int(x4), int(y4))

