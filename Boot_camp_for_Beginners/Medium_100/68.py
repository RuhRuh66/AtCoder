H, W = map(int, input().split())

root = H+W-1
c = 0
for i in range(H):
    temp = input()
    c += temp.count('#')
    
if c == root:
    print('Possible')
else:
    print('Impossible')
    