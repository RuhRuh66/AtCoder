S = input()



ans = 0
count=0
temp = 0
for i in S:
    if i =='B':
        temp += 1
    else:
        count += temp
        ans += count
        temp = 0

print(ans)