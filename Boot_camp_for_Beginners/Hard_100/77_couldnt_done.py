H, W, A, B = map(int, input().split())


for i in range(B):
    temp = '1'* A + '0' * (W-A)
    print(temp)
    
for j in range(B, H):
    temp = '0'*A+'1' * (W-A)
    print(temp)



