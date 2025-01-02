N, S = map(int, input().split())
A = list(map(int, input().split()))



def check(n, S):#ｎ個までの数字でＳが作れるかどうか確認。
    if n == 0:
        if S == 0:
            return True
        else:
            return False
    if S >= A[n-1] and check(n-1, S-A[n-1]):
        return True
    
    if check(n-1, S):
        return True
    else:
        return False
    

a = check(N, S)
if a:
    print('Yes')
else:
    print('No')