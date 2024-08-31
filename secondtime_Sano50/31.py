N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = str(input())

hands = [''] * N
score = 0

for i in range(K):
    machine = T[i]
    if machine == 'r':
        player = 'p'
        hands[i] = player
        score += P
    elif machine == 's':
        player = 'r'
        hands[i] = player
        score += R
        
    else:
        player = 's'
        hands[i] = player
        score += S
    
for i in range(K, N):
    machine = T[i]
    if machine == 'r':
        if hands[i-K] =='p':
            player = 'x'
            hands[i] = player
        else:
            player = 'p'
            hands[i] = player
            score += P
    
    elif machine == 's':
        if hands[i-K] == 'r':
            player = 'x'
            hands[i] = player
        else:
            player = 'r'
            hands[i] = player
            score += R
    else:
        if hands[i-K] == 's':
            player = 'x'
            hands[i] = player
        else:
            player = 's'
            hands[i] = player       
            score += S
            
            
print(score)