a, b = map(int, input().split())

ans = ''
if a>0 and b>0:
    ans = 'Positive'
    
elif a<=0 and b>=0:
    ans = 'Zero'
    
else:
    if (b-a+1)%2 == 0:
        ans = 'Positive'
    else:
        ans = 'Negative'
        
print(ans)