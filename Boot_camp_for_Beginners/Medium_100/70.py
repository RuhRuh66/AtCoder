x, y = map(int, input().split())

ab_x = abs(x)
ab_y = abs(y)

ab_dif = abs(ab_x - ab_y)

if ab_x < ab_y:
    if x >= 0 and y >0:
        ans = ab_dif
    elif x >= 0 and y < 0:
        ans = ab_dif + 1
    elif x < 0 and y > 0:
        ans = ab_dif + 1
    else:
        ans = ab_dif + 2
        
elif ab_x == ab_y:
    ans = 1
    
else:
    if x > 0 and y > 0:
        ans = ab_dif + 2
    elif x >0 and y<=0:
        ans = ab_dif + 1
    elif x < 0 and y > 0:
        ans = ab_dif + 1
    else:
        ans = ab_dif
        
print(ans)
        
        