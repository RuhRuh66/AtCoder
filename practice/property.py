def eratosthenes(limit: int, lowLimit:int = None):
    if lowLimit and (lowLimit <0 or lowLimit > limit):
        raise ValueError('incorrect lower limit')
    isPrime = [True] * (limit+1)
    isPrime[0] = False
    isPrime[1] = False
    for i in range(2, limit+1):
        if isPrime[i] == False:
            continue
        for j in range(i*i, limit+1, i):
            isPrime[j] = False
            
    if lowLimit:
        return [i for i, x in enumerate(isPrime[lowLimit:], start=lowLimit) if x]
    
    else:
        return [i for i, x in enumerate(isPrime) if x]
    

N = int(input())

est_max_prime = int(pow(N//12, 0.5))

prime_list = eratosthenes(est_max_prime)
cand_prime_nmbs = len(prime_list)

ans = 0
for i in range(cand_prime_nmbs-2):
    if pow(prime_list[i], 5) > N:
        break
    for j in range(i+1, cand_prime_nmbs-1):
        if pow(prime_list[i], 2) * pow(prime_list[j], 3) > N:
            break
        for k in range(j+1, cand_prime_nmbs):
            if pow(prime_list[i], 2) * prime_list[j] * pow(prime_list[k], 2 ) > N:
                break
            else:
                ans += 1
                
print(ans)
        
        


    