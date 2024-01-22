A, B, C, X, Y = map(int, input().split())

ans = 0
if A+B <= 2*C:
    ans = A * X + B * Y
else:
    if X < Y:
        ans = X * 2 * C + min( (Y-X)*B, (Y-X)*2*C)
    elif X == Y:
        ans = X * 2 * C
    else:
        ans = Y * 2 * C + min( (X-Y)*A, (X-Y)*2*C)

print(ans)