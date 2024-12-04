def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge_two_sorted_lists(left, right)



def merge_two_sorted_lists(a, b):
    i, j = 0, 0
    sorted_list = []
    len_a = len(a)
    len_b = len(b)
    
    while (i < len_a) and (j < len_b):
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1
            
    if i < len_a:
        sorted_list += a[i:] 
    if j < len_b:
        sorted_list += b[j:]
        
    return sorted_list
    
    
    

if __name__ == '__main__':
    arr = [10, 3, 15, 7, 8, 23, 98, 29]
    print(merge_sort(arr))
    
    
    
    