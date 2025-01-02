A, B = map(int, input().split())

if B >= A:
    A, B =B, A

n = A % B
while n != 0:
    A, B = B, n
    n = A % B

print(B)
