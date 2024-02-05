N, K = map(int, input().split())


rate = 0
win_prob = 0
for i in range(1, N+1):
    count = 0
    score = i
    while score < K:
        score *= 2
        count += 1
    win_prob += 1 / N * (0.5)**count
        
print(win_prob)
    
    
    