def eratosthenes(limit: int, minLimit: int = None):
    if minLimit and (minLimit<0 or minLimit < limit):
        raise ValueError('incorrect minLimit')
    isPrime = [True] * max(limit+1, 2)
    isPrime[0] = False
    isPrime[1] = False
    for i in range(2, limit+1):
        if not isPrime[i]:
            continue
        for j in range(i*i, limit+1, i):
            isPrime[j] = False
    if minLimit:
        return [i for i, x in enumerate(isPrime[minLimit:], start=minLimit) if x]
    else:
        return [i for i, x in enumerate(isPrime) if x]
    

print(eratosthenes(10))   