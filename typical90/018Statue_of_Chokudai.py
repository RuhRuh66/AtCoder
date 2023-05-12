
import math
import numpy

T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())

cho = numpy.array([X, Y, 0])

for i in range(Q):
    E = int(input())
    
    theta = E/T * 2*math.pi
    
    me = numpy.array([0, -L/2*math.sin(theta), L/2*(1-math.cos(theta))])
    g = numpy.array([0, -L/2*math.sin(theta), 0])
    
    g_to_cho = cho-g
    me_to_cho = cho-me
    
    x = numpy.inner(g_to_cho, me_to_cho)
    norm_g_to_cho = numpy.linalg.norm(g_to_cho)
    norm_me_to_cho = numpy.linalg.norm(me_to_cho)
    
    ans = numpy.arctan( L/2*(1-math.cos(theta))/norm_g_to_cho)
    
    print(math.degrees(ans))
    
    