N = int(input())

count = set()

for j in range(2, 34):
    for i in range(2, int(pow(N, 0.5))+1):
        if i ** j <= N:
            count.add(i**j)
        else:
            break
print(N-len(count))