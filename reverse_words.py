# -*- coding: utf8 -*-
"""
Input

The first line of input gives the number of cases, N.
N test cases follow. For each test case there will a line of letters and space characters indicating a list of space separated words. Spaces will not appear at the start or end of a line.

Output

For each test case, output one line containing "Case #x: " followed by the list of words in reverse order.

Limits

Small dataset

N = 5
1 ≤ L ≤ 25

Large dataset

N = 100
1 ≤ L ≤ 1000

Sample


Input

Output
3
this is a test
foobar
all your base
Case #1: test a is this
Case #2: foobar
Case #3: base your all
"""

def reverse_words(line):
    return ' '.join(line.strip().split()[::-1])

def main():
    f = open('B-large-practice.in')
    out = open('reverse-words.out', 'w')
    index = 1
    lines = []
    f.next()
    while True:
        try:
            lines.append("Case #%d: %s" % (index, reverse_words(f.next())))
            index += 1
        except StopIteration:
            break
    out.write('\n'.join(lines))
    out.close()

if __name__ == '__main__':
    main()

"""
Done!
Using python is cheating here. Need to try this again with a language with a bad string library like C.

Complexity: O(n*|s|)
Time - 0.037s(large), 0.002s (small)
"""
