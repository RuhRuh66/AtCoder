def matrix_multiply(A, B, mod):
    return [
        [(A[0][0]*B[0][0]+A[0][1]*B[1][0])%mod,
         (A[0][0]*B[0][1]+A[0][1]*B[1][1])%mod
         ], 
        [(A[1][0]*B[0][0]+A[1][1]*B[1][0])%mod,
         (A[1][0]*B[0][1]+A[1][1]*B[1][1])%mod
         ]
    ]


def matrix_power(A, n, mod):
    base = [[1, 0], [0, 1]]
    while n > 0:
        if n & 1 == 1:
            base = matrix_multiply(A, base, mod)
        A = matrix_multiply(A, A, mod)
        n = n>>1
    return base

def calc(A, n, mod):
    base =  matrix_power(A, n-2, mod)
    return (base[1][0] + base[1][1])

A = [[0, 1], [1, 2]]
mod = 1000000007

N = int(input())

print(calc(A, N, mod)%mod)

    
