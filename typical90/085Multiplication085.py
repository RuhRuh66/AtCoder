def divisors(n):
    div = set()
    m = 1
    while m**2 <= n:
        if n % m == 0:
            div.add(m)
            div.add(n//m)
        m += 1
        
    s = sorted(div)
    return s



def main():
    ans = 0
    k = int(input())
    divs = divisors(k)
    l = len(divs)
    for i in range(l):
        for j in range(i, l):
            a = divs[i]
            b = divs[j]
            
            if a * b > k:
                break
            if k//(a*b) < b:
                break
            if k%(a*b) == 0:
                ans += 1
                
    print(ans) 
            
if __name__ ==  '__main__':
    main()
    
