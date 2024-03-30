import timeit

import numpy

"""
Sum the numbers from 0 to n-1 in different ways.
Modified from @jamesmurphy-mc:
    https://github.com/mCodingLLC/VideosSampleCode/blob/master/videos/031_the_fastest_way_to_loop_in_python_an_unfortunate_truth/fastest_way_to_loop.py
"""

LIMIT=10_000_000


def while_loop(n: int=LIMIT) -> int:
    i = 0
    s = 0
    while i < n:
        s += i
        i += 1
    return s


def for_loop(n: int=LIMIT) -> int:
    s = 0
    for i in range(n):
        s += i
    return s


def for_loop_with_increment(n: int=LIMIT) -> int:
    s = 0
    for i in range(n):
        s += i
        i += 1
    return s


def for_loop_with_test(n: int=LIMIT) -> int:
    s = 0
    for i in range(n):
        if i < n: pass
        s += i
    return s


def for_loop_with_increment_and_test(n: int=LIMIT) -> int:
    s = 0
    for i in range(n):
        if i < n: pass
        i += 1
        s += i
    return s

def sum_range(n: int=LIMIT) -> int:
    return sum(range(n))


def sum_generator(n: int=LIMIT) -> int:
    return sum(i for i in range(n))


def sum_list_comp(n: int=LIMIT) -> int:
    return sum([i for i in range(n)])


def sum_numpy(n: int=LIMIT) -> int:
    return numpy.sum(numpy.arange(n, dtype=numpy.int64))


def sum_numpy_python_range(n: int=LIMIT) -> int:
    return numpy.sum(range(n))


def sum_math(n: int=LIMIT) -> int:
    return (n * (n - 1)) // 2


def main():
    print(f'Sum all numbers from 1 to {LIMIT:,}, measured in seconds')
    print('\twhile loop\t\t\t\t',
          timeit.timeit(while_loop, number=1))
    print('\tfor loop\t\t\t\t',
          timeit.timeit(for_loop, number=1))
    print('\tfor loop with unnecessary increment\t',
          timeit.timeit(for_loop_with_increment, number=1))
    print('\tfor loop with unnecessary test\t\t',
          timeit.timeit(for_loop_with_test, number=1))
    print('\tfor loop with both inc+test\t\t',
          timeit.timeit(for_loop_with_increment_and_test, number=1))
    print('\tsum of range\t\t\t\t',
          timeit.timeit(sum_range, number=1))
    print('\tsum using unnecessary generator\t\t',
          timeit.timeit(sum_generator, number=1))
    print('\tsum using list comprehension\t\t',
          timeit.timeit(sum_list_comp, number=1))
    print('\tnumpy sum\t\t\t\t',
          timeit.timeit(sum_numpy, number=1))
    print('\tnumpy sum python range\t\t\t',
          timeit.timeit(sum_numpy_python_range, number=1))
    print('\tpure math sum\t\t\t\t',
          timeit.timeit(sum_math, number=1))


if __name__ == '__main__':
    main()
