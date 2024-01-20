S = input()

N = len(S)

for i in range(2, N-1, 2):
    if S[:(N-i)//2] == S[(N-i)//2:N-i]:
        print(N-i)
        break
    