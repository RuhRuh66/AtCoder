N, A, B = map(int, input().split())

sums = 0
for i in range(N):
    str_i = str(i+1)
    gokei = 0
    for j in range(len(str_i)):
        gokei += int(str_i[j])
    if A <= gokei <= B:
        sums += i+1

print(sums)
    