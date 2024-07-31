import math


def f(r, temp):
    lg = math.log(r)
    return 1.129241e-3 + 2.341077e-4 * lg + 8.775468e-8 * (lg**3) - 1.0 / temp


def bisection(temp, relErr):

    lo, hi = (1e-9, 1e9)
    root = -1e9

    # print(f(lo,temp))
    # print(f(hi,temp))

    while True:
        nroot = (lo + hi) / 2
        nval = f(nroot, temp)

        if nval == 0:
            return nroot

        Err = abs(root - nroot) / nroot

        if Err < relErr:
            return nroot

        if nval < 0:
            lo = nroot
        else:
            hi = nroot

        root = nroot


def solve():
    relErr = 1e-9
    ans = bisection(19 + 273.15, relErr)

    assert abs(f(ans, 19 + 273.15)) < relErr

    print(ans)


if __name__ == '__main__':
    solve()
