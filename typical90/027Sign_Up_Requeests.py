N = int(input())


users = set()

for i in range(1, N+1):
    S = str(input())
    if S in users:
        continue
    else:
        print(i)
        users.add(S)
    