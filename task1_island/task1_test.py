#!/usr/bin/env python3

import task1

predef_isles = [
    ([[4, 5, 4],
      [3, 1, 5],
      [5, 4, 1]], 2),
    ([[5, 3, 4, 5],
      [6, 2, 1, 4],
      [3, 1, 1, 4],
      [8, 5, 4, 3]], 7),
    ([[2, 2, 2],
      [2, 1, 2],
      [2, 1, 2],
      [2, 1, 2]], 0)
]

if __name__ == '__main__':
    print('Testing trivial isles...')
    for test_isle, test_ans in predef_isles:
        ans = task1.get_water(test_isle)
        if ans != test_ans:
            print('Test case failed! Expected answer: {}, actual answer: {}'.format(test_ans, ans))
            