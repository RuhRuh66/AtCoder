N, M = map(int, input().split())

i = 1

denomis = []
while i*i < M:
    if M % i == 0:
        denomis.append(i)
        denomis.append(M//i)

    i += 1

if i**2 == M:
    denomis.append(i)

denomis.sort()

ans = 1
for t in denomis:
    if t<= M/N:
        ans = t
    else:
        break
print(ans)