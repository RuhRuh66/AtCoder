S = input()
S = list(S)

print('Yes' if S.count('W') == S.count('E') and S.count('S') == S.count('N') else 'No')