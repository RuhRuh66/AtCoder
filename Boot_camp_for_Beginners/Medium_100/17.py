N, T = map(int, input().split())

t = list(map(int, input().split()))

sum = 0
start = t[0]
end = t[0] + T

for i in range(1, N):
    if t[i] < end:
        end = t[i]-t[i-1] + end
    else:
        sum += end-start
        start = t[i]
        end = t[i] + T
sum += end - start

print(sum)