def main():
    import sys
    sys.setrecursionlimit(10 ** 9)
    input = sys.stdin.readline

    N, L = map(int,input().split())
    K = int(input())
    A = [0] + list(map(int,input().split())) + [L]
    
    # ようかんをXcm以上のK+1個のピースに分けられるか確認
    def check(l):
        left_idx, right_idx = 0, 0
        cnt = 0
        while right_idx < len(A):
            if A[right_idx] - A[left_idx] < l:
                right_idx += 1
            else:
                cnt += 1
                left_idx = right_idx
                right_idx += 1
                
        return True if cnt >= K+1 else False

    # Xの候補を二分探索
    ok, ng = 1,L+1
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid

    print(ok)

if __name__ == '__main__':
    main()N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

A.append(L)

ok = -1
ng = L
while ng-ok>1:
    mid = (ok+ng)//2
        