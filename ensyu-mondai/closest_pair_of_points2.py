def solution(x, y):
    a = list(zip(x, y)) #This produces list of tuples
    ax = sorted(a, key=lambda x: x[0]) #Presorting x-wise
    ay = sorted(a, key=lambda x: x[1]) #Presorting y-wise
    p1, p2, mi = closest_pair(ax, ay) # Recursive D&C function
    return mi

def closest_pair(ax, ay):
    ln_ax = len(ax) #It's quicker to assign variable
    if ln_ax <= 3:
        return brute(ax)  #A call to bruitforce comparison
    mid = ln_ax//2 #Division without reminder need int
    Qx = ax[:mid] #Two-part split
    Rx = ax[mid:]
    
    # Determine midpoint on x-axis
    midpoint = ax[mid][0]
    Qy = list()
    Ry = list()
    
    for x in ay: #split ay into 2 arrays using midpoint
        if x[0] <= midpoint:
            Qy.append(x)
        else:
            Ry.append(x)
            
            