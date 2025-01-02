X = int(input())

for i in range(-120, 120):
    for j in range(-120, 120):
        if pow(i, 5) - pow(j, 5) == X:
            print(i, j)