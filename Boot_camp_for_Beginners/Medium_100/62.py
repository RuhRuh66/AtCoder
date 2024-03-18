N = int(input())
A = list(map(int, input().split()))



from math import gcd

temp = A[0]
for i in range(1, N):
    temp = gcd(temp, A[i])

print(temp)

# B= A
# while len(B) > 1:
#     x = min(B)
#     C = []
#     for k in B:
#         if k % x == 0:
#             continue
#         else:
#             C.append(k%x)

#     C.append(x)
#     B = C
    
# print(*B)

    

    