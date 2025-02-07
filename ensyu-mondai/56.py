import numpy as np



def matrix_multiply(A, B, mod):   
    C = A@B%mod
    return C



def matrix_power(A, n, mod):
    base = np.array([[1,0,0], [0,1,0],[0,0,1]])
    while n > 0:
        if n & 1 == 1:
            base = A@base%mod
        A = matrix_multiply(A, A, mod)
        n = n >> 1
        
    return base

def calc(A, n, mod):
    a = np.array([[1], [1], [2]])
    base = matrix_power(A, n-3, mod)
    C = (base@a%mod)
    return C[2][0]

A = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]])
mod = 10**9+7
N = int(input())

print(calc(A, N, mod))