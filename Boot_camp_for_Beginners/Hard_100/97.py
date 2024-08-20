N  = int(input())

st = str()
if N == 0:
    print(0)
    exit()

while N != 1:
    if N >0:
        if N % 2 == 0:
            st = '0'+st
            N //= -2
        else:
            st = '1' + st
            N = -(N-1)//2
        
            
    else:
        if -N % 2 == 0:
            st = '0' + st
            N //= -2
            
        else:
            st = '1' + st
            N = (N-1) // -2
            
st = '1' + st
print(int(st))
