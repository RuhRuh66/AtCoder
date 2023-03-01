A, B, X = map(int, input().split())
def price(n):
    keta = len(str(n))
    return A * n + B * keta


def binary_search(ok, ng, X):
    min_price = price(1)
    max_price = price(10**9)
    if min_price > X:
        return 0

    elif max_price <= X:
        return 10**9
    
    else:
        while ng-ok >1:
            mid = (ok+ng)//2
            if price(mid) <= X:
                ok = mid
            else:
                ng = mid
                
        return ok

s = binary_search(1, 10**20, X)
print(s)
            
        