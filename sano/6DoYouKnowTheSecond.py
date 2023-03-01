N = int(input())
mountains = []
for i in range(N):
    name, height = map(str, input().split())
    mountains.append([name, int(height)])
    
mountains.sort(key=lambda x: x[1], reverse=True)
print(mountains[1][0])
