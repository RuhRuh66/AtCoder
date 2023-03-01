N = int(input())

def ten(x):
    flag = True
    while x > 0:
        if x % 10 == 7:
            flag = False
            break
        else:
            x //= 10
            
    return flag

def eight(x):
    flag = True
    while x > 0:
        if x % 8 == 7:
            flag = False
            break
        else:
            x //= 8
    return flag

count = 0
for i in range(1,N+1):
   if ten(i) and eight(i) == True:
       count += 1
       
print(count)