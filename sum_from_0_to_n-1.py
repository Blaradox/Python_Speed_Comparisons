import timeit

import numpy

"""
Sum the numbers from 0 to n-1 in different ways.
Courtesy of @jamesmurphy-mc:
    https://github.com/mCodingLLC/VideosSampleCode/blob/master/videos/031_the_fastest_way_to_loop_in_python_an_unfortunate_truth/fastest_way_to_loop.py
"""


def while_loop(n=100_000_000):
    i = 0
    s = 0
    while i < n:
        s += i
        i += 1
    return s


def for_loop(n=100_000_000):
    s = 0
    for i in range(n):
        s += i
    return s


def for_loop_with_increment(n=100_000_000):
    s = 0
    for i in range(n):
        s += i
        i += 1
    return s


def for_loop_with_test(n=100_000_000):
    s = 0
    for i in range(n):
        if i < n: pass
        s += i
    return s


def for_loop_with_increment_and_test(n=100_000_000):
    s = 0
    for i in range(n):
        if i < n: pass
        i += 1
        s += i
    return s


def main():
    print('while loop\t\t', timeit.timeit(while_loop, number=1))
    print('for pure\t\t', timeit.timeit(for_loop, number=1))
    # print('for inc\t\t\t', timeit.timeit(for_loop_with_increment, number=1))
    # print('for test\t\t', timeit.timeit(for_loop_with_test, number=1))
    # print('for inc+test\t', timeit.timeit(for_loop_with_increment_and_test, number=1))

if __name__ == '__main__':
    main()
