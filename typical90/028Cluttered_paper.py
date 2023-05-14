def is_rectangle(A:list, B:list):
    left = max(A[0], B[0])
    bottom = max(A[1], B[1])
    right = min(A[2], B[2])
    ceil = min(A[3], B[3])
    if left < right and bottom < ceil:
        area = (right-left) * (ceil-bottom)
        return area
    else:
        return 0