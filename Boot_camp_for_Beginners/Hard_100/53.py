from collections import defaultdict

def main():
    n = int(input())
    if n <= 2:
        print(1)
        exit()
    b = [tuple(map(int, input().split())) for _ in range(n)]
    b.sort()
    
    m = defaultdict(int)
    
    for i in range(n-1):
        sx, sy = b[i]
        for j in range(i+1, n):
            tx, ty = b[j]
            
            m[(sx-tx, sy-ty)]+= 1
            
    print(n-max(m.values()))
    

if __name__ == '__main__':
    main()

