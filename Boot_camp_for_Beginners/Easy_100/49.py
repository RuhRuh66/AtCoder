H, W = map(int, input().split())

A = []

for i in range(H):
    temp = input()
    A.append(temp)
    
print('#' * (W+2))
for j in range(H):
    s = '#' + A[j] +'#'
    print(s)
print('#' * (W+2))

    