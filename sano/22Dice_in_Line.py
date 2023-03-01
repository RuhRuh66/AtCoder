N, K = map(int, input().split())
p = list(map(int, input().split()))

converted_p = []
for i in range(N):
    ex = ((p[i]+1)*p[i])/(p[i]*2)
    converted_p.append(ex)
 

cumulative_sum = [0] * N
cumulative_sum[0] = converted_p[0]
for i in range(1, N):
    cumulative_sum[i] = cumulative_sum[i-1] + converted_p[i]

max_sum = cumulative_sum[K-1]
for i in range(K, N):
    max_sum = max(max_sum, cumulative_sum[i]-cumulative_sum[i-K])
    
print(max_sum)



    
    