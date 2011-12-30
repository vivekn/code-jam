# -*- coding: utf8 -*-
"""
Google store credit problem:
nput

The first line of input gives the number of cases, N. N test cases follow. For each test case there will be:

One line containing the value C, the amount of credit you have at the store.
One line containing the value I, the number of items in the store.
One line containing a space separated list of I integers. Each integer P indicates the price of an item in the store.
Each test case will have exactly one solution.
Output

For each test case, output one line containing "Case #x: " followed by the indices of the two items whose price adds up to the store credit. The lower index should be output first.

Limits

5 ≤ C ≤ 1000
1 ≤ P ≤ 1000

Small dataset

N = 10
3 ≤ I ≤ 100

Large dataset

N = 50
3 ≤ I ≤ 2000

Sample


Input

3
100
3
5 75 25
200
7
150 24 79 50 88 345 3
8
8
2 1 9 4 4 56 90 3

Output

Case #1: 2 3
Case #2: 1 4
Case #3: 4 5

"""
from collections import defaultdict

def process_case(credit, items):
    complement = lambda n : credit - n
    item_cnt = defaultdict(int)
    indices = defaultdict(list)
    for n, item in enumerate(items):
        item_cnt[item] += 1
        indices[item].append(n)
    for item in items:
        if complement(item) in item_cnt:
            if item == complement(item):
                if item_cnt[item] > 1:
                    return sorted((indices[item].pop() + 1, indices[item].pop() + 1))
            else:
                return sorted((indices[item].pop() + 1, indices[complement(item)].pop() + 1))

def main():
    f = open('A-small-practice.in')
    out = open('store-credit.out', 'w')
    index = 1
    lines = []
    f.next()
    while True:
        try:
            credit = int(f.next().strip())
            n_items = f.next()
            items = map(int, f.next().strip().split())
            x, y = process_case(credit, items)
            lines.append("Case #%d: %d %d" % (index, x, y))
            index += 1
        except StopIteration:
            break
    out.write('\n'.join(lines))
    out.close()


if __name__ == '__main__':
    main()

"""
Done!

Complexity - O(n)
Time - 0.111s (large), 0.043s (small)
"""


