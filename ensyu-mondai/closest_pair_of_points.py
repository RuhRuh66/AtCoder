def euclidean_dist_sqr(point1, point2):
    return (point1[0]-point2[0])** 2 +  (point1[1]-point2[1])** 2

def column_based_sort(array, column=0):
    return sorted(array, key=lambda x:x[column])

    
def bruit_force_closest_pair(points, points_counts, min_dis=float('inf')):
    for i in range(points_counts-1):
        for j in range(i+1 ,points_counts):
            current_dist = euclidean_dist_sqr(points[i], points[j])
            min_dis = min(min_dis, current_dist)
            
def dis_between_closest_in_strip(points, points_counts, min_dis=float('inf')):
    for i in range(min(6, points_counts-1), points_counts):
        for j in range(max(0, i-6), i):
            current_dist = euclidean_dist_sqr(points[i], points[j])
            min_dis = min(min_dis, current_dist)
            return min_dis
        
def closest_pair_of_points_sqr(points_sorted_on_x, points_sorted_on_y, points_counts):
    # base case
    if points_counts <=3:
        return bruit_force_closest_pair(points_sorted_on_x, points_counts)
    # recursion
    mid = points_counts // 2
    
    