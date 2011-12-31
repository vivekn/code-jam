"""
Problem

A company is located in two very tall buildings. The company intranet connecting the buildings consists of many wires, each connecting a window on the first building to a window on the second building.

You are looking at those buildings from the side, so that one of the buildings is to the left and one is to the right. The windows on the left building are seen as points on its right wall, and the windows on the right building are seen as points on its left wall. Wires are straight segments connecting a window on the left building to a window on the right building.



You've noticed that no two wires share an endpoint (in other words, there's at most one wire going out of each window). However, from your viewpoint, some of the wires intersect midway. You've also noticed that exactly two wires meet at each intersection point.

On the above picture, the intersection points are the black circles, while the windows are the white circles.

How many intersection points do you see?

Input

The first line of the input gives the number of test cases, T. T test cases follow. Each case begins with a line containing an integer N, denoting the number of wires you see.

The next N lines each describe one wire with two integers Ai and Bi. These describe the windows that this wire connects: Ai is the height of the window on the left building, and Bi is the height of the window on the right building.

Output

For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is the number of intersection points you see.

Limits

1 ≤ T ≤ 15.
1 ≤ Ai ≤ 104.
1 ≤ Bi ≤ 104.
Within each test case, all Ai are different.
Within each test case, all Bi are different.
No three wires intersect at the same point.

Small dataset

1 ≤ N ≤ 2.

Large dataset

1 ≤ N ≤ 1000.

Sample


Input

Output

2
3
1 10
5 5
7 7
2
1 1
2 2
Case #1: 2
Case #2: 0


"""

def intersects(pt1, pt2):
    """
    Checks if the two ropes intersect
    """
    [pt_b , pt_a] = sorted([pt1, pt2])
    a, b = pt_a
    c, d = pt_b
    if b > d: return False
    return True

def count(points):
    return [intersects(point, other) for point in points for other in points if point != other].count(True) / 2

def main():
    f = open('rope-large.in')
    out = open('rope.out', 'w')
    index = 1
    lines = []
    f.next()
    while True:
        try:
            n = int(f.next())
            points = [tuple(map(int, f.next().split())) for i in range(n)]
            lines.append("Case #%d: %d" % (index, count(points)))
            index += 1
        except StopIteration:
            break
    out.write('\n'.join(lines))
    out.close()

if __name__ == '__main__':
    main()

"""
Complexity: O(n ^ 2)
This is slow, but the limits of the problem are small as well. If
n is large, an interval tree would be a good idea.

Time - 20.601s(large), 0.002s(small)
"""
