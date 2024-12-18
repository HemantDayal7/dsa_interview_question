# Convex Hull Finder using Graham Scan Algorithm

This repository contains a Python implementation of the Graham Scan algorithm for finding the convex hull of a set of points in a 2-D plane.

## Problem Description

Given a set of points in a 2-D plane, the task is to find the smallest convex polygon that contains all of the points. The polygon formed should be convex, meaning all of its interior angles must be less than 180 degrees.

### Constraints:
- The solution polygon must contain all of the given points.
- The solution polygon must be the smallest possible convex polygon that contains all of the given points.
- The solution polygon must be unique.

### Examples:
**Input:**
[(100000,1000), (20000,3000), (30000,2000), (4,4000), (5,1000)]

**Output:**
[(5, 1000), (100000, 1000), (4, 4000)]


## Implementation

We have provided a Python implementation of the Graham Scan algorithm to solve the convex hull problem efficiently. The algorithm involves the following steps:
1. Find the point with the lowest y-coordinate (and the leftmost such point in case of a tie) as the reference point.
2. Sort the remaining points by the angle they make with the reference point in counterclockwise order.
3. Consider each point in order. If the point forms a left turn with the previous two points, add it to the convex hull; otherwise, skip it.
4. After processing all points, the convex hull is formed.

## Usage

To use the provided implementation, simply execute the Python script `convex_hull.py` and provide a list of points as input. The script will return the convex hull points in counterclockwise order.

## Contributing

Contributions are welcome! Feel free to open a pull request with any improvements or additional features.

