# -*- coding: utf8 -*-
"""
Problem

After years of study, scientists at Google Labs have discovered an alien language transmitted from a faraway planet. The alien language is very unique in that every word consists of exactly L lowercase letters. Also, there are exactly D words in this language.

Once the dictionary of all the words in the alien language was built, the next breakthrough was to discover that the aliens have been transmitting messages to Earth for the past decade. Unfortunately, these signals are weakened due to the distance between our two planets and some of the words may be misinterpreted. In order to help them decipher these messages, the scientists have asked you to devise an algorithm that will determine the number of possible interpretations for a given pattern.

A pattern consists of exactly L tokens. Each token is either a single lowercase letter (the scientists are very sure that this is the letter) or a group of unique lowercase letters surrounded by parenthesis ( and ). For example: (ab)d(dc) means the first letter is either a or b, the second letter is definitely d and the last letter is either d or c. Therefore, the pattern (ab)d(dc) can stand for either one of these 4 possibilities: add, adc, bdd, bdc.

Input

The first line of input contains 3 integers, L, D and N separated by a space. D lines follow, each containing one word of length L. These are the words that are known to exist in the alien language. N test cases then follow, each on its own line and each consisting of a pattern as described above. You may assume that all known words provided are unique.

Output

For each test case, output

Case #X: K
where X is the test case number, starting from 1, and K indicates how many words in the alien language match the pattern.

Limits

Small dataset

1 ≤ L ≤ 10
1 ≤ D ≤ 25
1 ≤ N ≤ 10
Large dataset

1 ≤ L ≤ 15
1 ≤ D ≤ 5000
1 ≤ N ≤ 500
Sample


Input

Output

3 5 4
abc
bca
dac
dbc
cba
(ab)(bc)(ca)
abc
(abc)(abc)(abc)
(zyx)bc
Case #1: 2
Case #2: 1
Case #3: 3
Case #4: 0

"""

def match_pattern(word_list, pattern):
    targets = word_list
    test = []
    paren = False
    index = 0
    while pattern:
        if paren and pattern[0] != ')':
            test.append(pattern[0])
            pattern = pattern[1:]
            continue
        elif paren and pattern[0] == ')':
            pattern = pattern[1:]
            prune = lambda char : set([word for word in targets if word[index] == char])
            targets = reduce(lambda acc, x: acc | x, map(prune, test))
            index += 1
            paren = False
            continue
        elif pattern[0] == '(':
            pattern = pattern[1:]
            test = []
            paren = True
            continue
        else:
            char = pattern[0]
            pattern = pattern[1:]
            targets = set(word for word in targets if word[index] == char)
            index += 1

    return len(targets)

def main():
    f = open('alien-large.in')
    out = open('alien.out', 'w')
    index = 1
    lines = []
    _, d, n = map(int, f.next().split())
    while True:
        try:
            dictionary = [f.next().strip() for i in range(d)]
            words = [f.next().strip() for i in range(n)]
            for word in words:
                lines.append("Case #%d: %d" % (index, match_pattern(dictionary, word)))
                index += 1
        except StopIteration:
            break
    out.write('\n'.join(lines))
    out.close()

if __name__ == '__main__':
    main()

"""
    Complexity - O(n)
    Time - 29.081s(large) / 11.2s (PyPy),  0.002s(small)
    Need a faster algo than this
"""
