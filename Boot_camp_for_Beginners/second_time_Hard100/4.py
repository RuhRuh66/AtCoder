a, b,x = map(int, input().split())

def c(n):
    if n == -1:
        return 0
    else:
        return n//x + 1

print(c(b)-c(a-1))
