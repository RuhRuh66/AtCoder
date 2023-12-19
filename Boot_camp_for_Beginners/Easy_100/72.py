X = int(input())

max_b = 34
max_p = 11

ans = 0
for i in range(1, max_b):
    for j in range(2, max_p):
        if i ** j <= X:
            ans = max(ans, i**j)
        else:break

print(ans)


    
            