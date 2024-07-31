import math


def f (t):
    return 2000 * math.log ( 140000 / (140000 - 2100 * t)) - 9.8 * t

def integrationTrapezoidal (a, b, n):
    ans = f(a) + f(b)
    h = (b - a) / n

    for i in range(n-1):
        a += h
        ans += 2 * f(a)

    return ans * h / 2

if __name__ == '__main__':
    n = int(input())
    print("Integrated Value = ", integrationTrapezoidal(8, 30, n))
    print()
    prev = 0
    for i in range(1,6):
        cur = integrationTrapezoidal(8, 30, i)
        print("For n = ",i,", Calculated Value = ",cur,", Absolute approximate relative error = ",end = "")
        if i == 1:
            print("N/A")
        else:
            print(abs(cur - prev) / cur * 100,"%")
        prev = cur
