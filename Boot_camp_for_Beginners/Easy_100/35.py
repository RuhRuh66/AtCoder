S = input()
S = list(S)
S = set(S)
alpa = [chr(i) for i in range(97, 123)]

for j in S:
    if j in alpa:
        alpa.remove(j)
        
if len(alpa) == 0:
    print('None')
else:
    print(alpa[0])