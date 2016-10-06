#!/usr/bin/env python3

import task1
from random import randint

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
    print('Generating random islands to check for crashes...')
    TEST_NR = 999999
    for i in range(TEST_NR):
        x_size = randint(1, 50)
        y_size = randint(1, 50)
        isle = [[randint(1, 1000) for x in range(x_size)] for y in range(y_size)]
        ans = task1.get_water(isle)
        if i % 500 == 0:
            print('Survived {} tests...'.format(i))