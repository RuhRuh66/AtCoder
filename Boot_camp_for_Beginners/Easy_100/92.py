S = input()

S = list(str(S))

a = len(S)

if a == 0 or a == 1:
    print(0)
    exit()
else:
    red = S.count('0')
    blue = S.count('1')
    print(min(red, blue)*2)
    
    
