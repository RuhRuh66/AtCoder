import math

# Function to find the distance between two points
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Function to find the closest pair in a strip
def closest_in_strip(strip, d):
    min_dist = d  # Initialize the minimum distance as d

    # Sort the strip according to the y coordinate
    strip.sort(key=lambda point: point[1])

    # Compare each point to the next points in the strip within the range limited by 7
    for i in range(len(strip)):
        for j in range(i + 1, min(i + 7, len(strip))):
            if (strip[j][1] - strip[i][1]) < min_dist:
                min_dist = min(min_dist, distance(strip[i], strip[j]))

    return min_dist

# Function to find the closest pair of points using divide and conquer
def closest_pair_util(points_sorted_by_x, points_sorted_by_y):
    n = len(points_sorted_by_x)

    # Base case: If there are 2 or 3 points, use a brute force approach
    if n <= 3:
        min_dist = float('inf')
        for i in range(n):
            for j in range(i + 1, n):
                min_dist = min(min_dist, distance(points_sorted_by_x[i], points_sorted_by_x[j]))
        return min_dist

    # Find the midpoint
    mid = n // 2
    midpoint = points_sorted_by_x[mid]

    # Divide points into two halves
    left_half_x = points_sorted_by_x[:mid]
    right_half_x = points_sorted_by_x[mid:]

    # Keep points sorted by y-coordinate
    left_half_y = list(filter(lambda point: point[0] <= midpoint[0], points_sorted_by_y))
    right_half_y = list(filter(lambda point: point[0] > midpoint[0], points_sorted_by_y))

    # Recursively find the closest pairs in the left and right halves
    d1 = closest_pair_util(left_half_x, left_half_y)
    d2 = closest_pair_util(right_half_x, right_half_y)

    # Find the minimum distance in both halves
    d = min(d1, d2)

    # Create a strip containing points close to the dividing line
    strip = [point for point in points_sorted_by_y if abs(point[0] - midpoint[0]) < d]

    # Find the closest pair in the strip
    return min(d, closest_in_strip(strip, d))

# Main function to find the closest pair of points
def closest_pair(points):
    points_sorted_by_x = sorted(points, key=lambda point: point[0])
    points_sorted_by_y = sorted(points, key=lambda point: point[1])
    return closest_pair_util(points_sorted_by_x, points_sorted_by_y)

# Example usage
points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
result = closest_pair(points)
print(f"The smallest distance is {result}")