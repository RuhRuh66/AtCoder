N, A, B = map(int, input().split())

quotient = N // (A+B)
reminder = N % (A+B)

ans = 0

if reminder <= A:
    ans = quotient * A + reminder
else:
    ans = quotient*A + A
    
print(ans)

