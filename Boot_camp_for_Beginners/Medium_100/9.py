A, B, C = map(int, input().split())

mods = set()

for i in range(1, 101):
    temp = (A * i) % B
    if temp not in mods:
        mods.add(temp)
        
    else:
        break
if C in mods:
    print('YES')
else:
    print('NO')