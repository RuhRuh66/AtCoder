Sp = input()
T = input()

s = len(Sp)
t = len(T)

for i in range(s-t, -1, -1):
    target = Sp[i:i+t]
    flag = True
    for j in range(t):
        if target[j] == T[j]:
            continue
        elif target[j] == '?':
            continue
        else:
            flag = False
            break
    if flag == True:
        pre_ans = Sp[:i] + T + Sp[i+t:]
        ans = pre_ans.replace('?', 'a')
        print(ans)
        exit()
        
print('UNRESTORABLE')
        

            
        