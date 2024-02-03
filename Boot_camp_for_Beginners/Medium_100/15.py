S = input()
import re

k = 'keyence'

a = '.*'

for i in range(8):
    w = '^'+k[:i] + a + k[i:]+'$'
    wc = re.compile(w)
    
 
    if re.match(wc, S):
        print('YES')
        exit()
        
print('NO')


