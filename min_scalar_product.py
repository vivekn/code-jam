# -*- coding: utf8 -*-
"""
Problem

You are given two vectors v1=(x1,x2,...,xn) and v2=(y1,y2,...,yn). The scalar product of these vectors is a single number, calculated as x1y1+x2y2+...+xnyn.

Suppose you are allowed to permute the coordinates of each vector as you wish. Choose two permutations such that the scalar product of your two new vectors is the smallest possible, and output that minimum scalar product.

Input

The first line of the input file contains integer number T - the number of test cases. For each test case, the first line contains integer number n. The next two lines contain n integers each, giving the coordinates of v1 and v2 respectively.
Output

For each test case, output a line

Case #X: Y
where X is the test case number, starting from 1, and Y is the minimum scalar product of all permutations of the two given vectors.
Limits

Small dataset

T = 1000
1 ≤ n ≤ 8
-1000 ≤ xi, yi ≤ 1000

Large dataset

T = 10
100 ≤ n ≤ 800
-100000 ≤ xi, yi ≤ 100000

Sample


Input

Output

2
3
1 3 -5
-2 4 1
5
1 2 3 4 5
1 0 1 0 1

Case #1: -25
Case #2: 6

"""
from heapq import heapify, heappop

def min_scalar_product(vec1, vec2):
    heapify(vec1) # min-heap
    vec2 = [-1 * x for x in vec2]
    heapify(vec2) # max-heap
    msp = 0
    while vec1 and vec2:
        msp += (heappop(vec1) * heappop(vec2) * -1)
    return msp

def main():
    f = open('msp-large.in')
    out = open('msp-out2', 'w')
    index = 1
    lines = []
    f.next()
    while True:
        try:
            f.next()
            vec1 = map(int, f.next().strip().split())
            vec2 = map(int, f.next().strip().split())
            lines.append("Case #%d: %d" % (index, min_scalar_product(vec1, vec2)))
            index += 1
        except StopIteration:
            break
    out.write('\n'.join(lines))
    out.close()

if __name__ == '__main__':
    main()

"""
Done!

Complexity: O(n log n)
Time: - 0.111s(large), 0.015s(small)
"""
