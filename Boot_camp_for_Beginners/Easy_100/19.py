N, M, X = map(int, input().split())

A = list(map(int, input().split()))


count = 0

for i in A:
    if i<X:
        count+=1
    else:
        break
print(min(count, len(A)-count))


    


