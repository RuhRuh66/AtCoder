N = int(input())

A = list(map(int, input().split()))


count = 0

judge = True

while judge:
    if all([i%2==0 for i in A]):
        count += 1
        A = [i//2 for i in A]
    else:
        judge = False
        
print(count)