N, K = map(int, input().split())
R, S, P  = map(int, input().split())
T = input()
my_card = ['x'] * N

for i in range(N):
    if i < K:
        if T[i] == 'r':
            my_card[i] = 'P'
        elif T[i] == 's':
            my_card[i] = 'R'
        else:
            my_card[i] = 'S'
            
    else:
        if T[i] == 'r':
            if my_card[i-K] != 'P':
                my_card[i] = 'P'
            else:
                continue
        elif T[i] == 's':
            if my_card[i-K] != 'R':
                my_card[i] = 'R'
            else:
                continue
        else:
            if my_card[i-K] != 'S':
                my_card[i] = 'S'
            else:
                continue
            

print(my_card.count('R')*R + my_card.count('S')*S + my_card.count('P')*P)   

 