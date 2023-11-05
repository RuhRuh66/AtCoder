N = int(input())
D, X = map(int, input().split())

consumed = 0
for i in range(N):
    A = int(input())
    consumed += (1+(D-1)//A)
    

print(consumed+X)
    