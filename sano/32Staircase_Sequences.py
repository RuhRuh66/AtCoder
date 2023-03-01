N = int(input())

i = 1
count_plus = 0
while i**2 <= 2*N:
    if 2* N % i == 0 and (i + 2*N//i)%2 == 1:
        count_plus+=1
    i += 1
        
print(count_plus*2)