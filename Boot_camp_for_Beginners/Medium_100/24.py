N, A, B = map(int, input().split())

if A>B:
    print(0)
    exit()

elif N == 1 and A != B:
    print(0)
    exit()
    
elif N == 1 and A == B:
    print(1)
    exit()
  
else:
    ans = (B-A) * (N-2) + 1
    

print(ans)