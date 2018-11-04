from functools import cmp_to_key

def translatePoints(points, x, y):
    """Translates the coordinates of points."""
    for point in points:
        point[0] += x
        point[1] += y

def comparator(p1, p2):
    """The comparator used for the sorting"""
    value = p1[0] * p2[1] - p2[0] * p1[1]

    if value < 0:
        return -1
    elif value > 0:
        return 1
    else:
        return 0

# The set of points to check
points = [[-2, 5], [1, 2], [2, 1], [2, -2], [0, 0]]

# Smallest triangle area
smallestArea = float("+inf")

# For every point
for i in range(len(points)):
    point = points[i]
    x, y = point[0], point[1]

    # Translate all points so that our point is origin
    translatePoints(points, -x, -y)

    comparisonArray = sorted(list(points), key=cmp_to_key(comparator))
    del(comparisonArray[i]) # Delete the [0, 0] point

    # Check all of the neighbouring points
    for j in range(0, len(comparisonArray) - 1):
        p1 = comparisonArray[j]
        p2 = comparisonArray[j + 1]

        # Compute the area and check wheter it isn't smallest
        area = 1/2 * abs(p1[0] * p2[1] - p1[1] * p2[0])
        if area != 0 and area < smallestArea:
            smallestArea = area

    # Translate back
    translatePoints(points, x, y)

print("The minimum triangle are is "+str(smallestArea)+".")
