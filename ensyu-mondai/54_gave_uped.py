def matrix_multiply(A, B, mod):
    return [
        [(A[0][0]*B[0][0] + A[0][1]*B[1][0])%mod, (A[0][0]*B[0][1] + A[0][1]*B[1][1])%mod],
        [(A[1][0]*B[0][0] + A[1][1]*B[1][0])%mod,(A[1][0]*B[0][1] + A[1][1]*B[1][1])%mod]
    ]

def matrix_power(A, n, mod):
    result = [[1,0], [0, 1]]
    while n>0:
        if n & 1 == 1:
            result = matrix_multiply(result, A, mod)
        A = matrix_multiply(A, A, mod)
        n = n >> 1
    return result


def fibonacci(n, mod):
    base_matrix = [[1, 1], [1, 0]]
    powered_matrix = matrix_power(base_matrix, N-1, mod)
    return powered_matrix[0][0]

        
        