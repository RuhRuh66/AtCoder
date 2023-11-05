S = input()

l = len(S)

best = 10000
for i in range(0, l-2):
    temp = int(''.join([S[i], S[i+1], S[i+2]]))
    best = min(best, abs(temp-753))

print(best)
    

