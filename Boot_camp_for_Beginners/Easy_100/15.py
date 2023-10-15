N = int(input())

d = list(map(int, input().split()))
d.sort()



import statistics
if statistics.median_high(d) == statistics.median_low(d):
    print(0)
    exit()
else:    
    print(statistics.median_high(d)-statistics.median_low(d))

