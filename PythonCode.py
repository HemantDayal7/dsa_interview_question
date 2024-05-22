from math import atan2
import random
import timeit

def graham_scan(points):
    def cross(a, b, c):
        return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

    if len(points) < 3:
        return points

    # find the point with the lowest y-coordinate
    lowest = min(points, key=lambda p: (p[1], p[0]))

    # sort the remaining points by angle with respect to the lowest point
    sorted_points = sorted(points, key=lambda p: (atan2(p[1] - lowest[1], p[0] - lowest[0]), p[0] ** 2 + p[1] ** 2))

    # create a stack for the hull points and add the first three points
    hull = [lowest, sorted_points[0]]
    for i in range(1, len(sorted_points)):
        while len(hull) > 1 and cross(hull[-2], hull[-1], sorted_points[i]) <= 0:
            hull.pop()
        hull.append(sorted_points[i])

    return hull

# example usage
points = [(10,900), (7000,300), (500,9), (400,4), (9,300)]
hull = graham_scan(points)
print(hull)
print("Running time: {:.5f} microseconds".format(timeit.timeit(lambda: graham_scan(points), number=1000000)))
