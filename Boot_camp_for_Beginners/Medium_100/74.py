N = int(input())

L = []
S = []
for i in range(N):
    temp = input()
    temp_l = list(temp)
    temp_s = set(temp)
    L.append(temp_l)
    S.append(temp_s)

chr_set = sorted(list(set.intersection(*S)))

from collections import defaultdict
ch_dict = defaultdict(int)
                      
for ch in chr_set:
    ch_num_min = 10*10
    for j in L:
        ch_num_min = min(ch_num_min, j.count(ch))
    ch_dict[ch] = ch_num_min

ans = ''
for ch, num in ch_dict.items():
    ans += ch * num

print(ans)


