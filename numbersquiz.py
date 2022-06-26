#!/usr/bin/env python


import functools


def remove(l, i):
    return l[0:i] + l[i + 1:]


def permutations(l):
    if len(l) == 0:
        return []
    elif len(l) == 1:
        return [ l ]
    else:
        l1 = []
        for i in range(len(l)):
            for p in permutations(remove(l, i)):
                l1 += [ [ l[i] ] + p ]
        return l1


def expressions(l):
    def expressions(a, l):
        if len(l) == 0:
            return a
        else:
            a1 = []
            for e in a:
                a1 += [ e + [ '+', l[0] ] ]
                a1 += [ e + [ '-', l[0] ] ]
                a1 += [ e + [ '*', l[0] ] ]
                a1 += [ e + [ '/', l[0] ] ]
            return expressions(a1, l[1:])
    return expressions([ [ l[0] ] ], l[1:])


def calculate(l):
    def calculate(a, l):
        if len(l) == 0:
            return a
        else:
            if l[0] == '+':
                return calculate(a + l[1], l[2:])
            elif l[0] == '-':
                return calculate(a - l[1], l[2:])
            elif l[0] == '*':
                return calculate(a * l[1], l[2:])
            elif l[0] == '/' and a % l[1] == 0:
                return calculate(a / l[1], l[2:])
    return calculate(l[0], l[1:])


def numbersquiz(l, a):
    ps = permutations(l)
    es = functools.reduce(lambda a, e: a + expressions(e), ps, [])
    es1 = filter(lambda e: calculate(e) == a, es)
    return es1


def main(argv, stdin, stdout):
    if len(argv) != 8:
        print('Usage: numbersquiz n1 n2 n3 n4 n5 n6 a')
        return 1

    ns = list(map(int, argv[1:7]))
    a = int(argv[7])
    for e in numbersquiz(ns, a):
        print(e)

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv, sys.stdin, sys.stdout))
