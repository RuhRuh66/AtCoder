def eratosthenes(X):
    is_prime = [True for i in range(X+1)]
    is_prime[0] = False
    is_prime[1] = False
    
    j = 2
    while j**2 < X:
        if is_prime[j] == True:
            for k in range(j*j, X+1, j):
                is_prime[k] = False
        j += 1
    
    return [i for i, x in enumerate(is_prime) if x]
                

X = int(input())

s = eratosthenes(2*X)

for i in s:
    if i>=X:
        print(i)
        exit()
                