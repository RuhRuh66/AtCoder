N = int(input())

jobs = []
for i in range(N):
    k, j = map(int, input().split())
    jobs.append((k, j))
    
jobs.sort(key= lambda x: x[1])

total_job_time = 0
for l, m in jobs:
    total_job_time += l
    if total_job_time<= m:
        continue
    else:
        print('No')
        exit()
        
print('Yes')

    
    
