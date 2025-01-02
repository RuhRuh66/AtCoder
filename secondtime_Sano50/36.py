N, K = map(int, input().split())
A = [0]+list(map(int, input().split()))

now = 1
seq = set()
seq.add(1)
seq_l = [1]
cnt = 0
for i in range(N):
    next = A[now]
    if next not in seq:
        cnt += 1
        seq.add(next)
        seq_l.append(next)
        now = next
    else:
        total_length = len(seq_l)
        pre = seq_l.index(next)
        cycles = total_length - pre
        cycle_seq = seq_l[pre:]
        break


# print(total_length, pre, cycles, seq_l, cycle_seq)
    
if K <= total_length-1:
    ans = seq_l[K]
else:
    ans = cycle_seq[(K-pre)%cycles]
    
print(ans)
        

    
    
    