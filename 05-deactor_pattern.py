# -*-coding: utf-8 -*-


def fibonacci(n):
    """Fibonacci数列"""
    assert(n >= 0), 'n must be >= 0'
    return n if n in (0, 1) else fibonacci(n-1) + fibonacci(n-2)


# if __name__ == '__main__':
#     from timeit import Timer
#     t = Timer('fibonacci(8)', 'from __main__ import fibonacci')
#     print t.timeit()  # 7.48872545315


"""使用memoization方法进行改良"""

know = {0:0, 1:1}


def fib(n):
    assert(n >= 0), "n must >= 0"
    if n in know:
        return know[n]
    res = fib(n-1) + fib(n-2)
    know[n] = res
    return know


# if __name__ == '__main__':
#     from timeit import Timer
#     t = Timer("fib(100)", "from __main__ import fib")
#     print t.timeit()  # 0.33223


import functools


def memoize(fn):
    """装饰器"""
    know = dict()

    @functools.wraps(fn)
    def memoizer(*args):
        if args not in know:
            know[args] = fn(*args)
        return know[args]
    return memoizer


@memoize
def nsum(n):
    return 0 if n == 0 else n + nsum(n-1)


@memoize
def fibn(n):
    """返回 fibn 的第n个数"""
    assert(n >= 0), 'n must be >= 0'
    return n if n in (0, 1) else fibn(n - 1) + fibn(n - 2)


if __name__ == '__main__':
    from timeit import Timer
    measure = [{'exec': 'fibn(100)', "import": 'fibn', 'func': 'fibn'},
               {'exec': 'nsum(200)', 'import': 'nsum', 'func': 'nsum'}]
    for m in measure:
        t = Timer("{}".format(m['exec'], 'from __main__ import {}'.format(m['import'])))
        print "name: {}, doc: {}, executing: {}, time: {}".format(m['func'], m['func'], t.timeit())