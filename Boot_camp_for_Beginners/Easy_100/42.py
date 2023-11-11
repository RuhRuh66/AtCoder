N, M = map(int, input().split())
temp = list(map(int, input().split()))
temp_set = set(temp[1:])
for i in range(1, N):
    temp2 = list(map(int, input().split()))
    temp_set2  =set(temp2[1:])
    temp_set = temp_set & temp_set2
    
print(len(temp_set))