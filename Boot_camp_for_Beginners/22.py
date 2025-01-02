S = list(input())
T = list(input())


alp = [chr(i) for i in range(97, 123)]

  
sc = []
tc = []

for j in range(26):
    sc.append(S.count(alp[j]))
    tc.append(T.count(alp[j]))
    

sc.sort()
tc.sort()

if sc == tc:
    print('Yes')
else:
    print('No')

