import matplotlib.pyplot as plt
import numpy as np
from sympy import *

def L(x, val_x):
    ans = []
    n = len(val_x)
    for i in range(n):
        temp = 1
        for j in range(n):
            if(i!=j):
                temp = temp*(x-val_x[j])/(val_x[i]-val_x[j])
        ans.append(temp)
    return ans

def f_newton(val_x, val_y):
    n = len(val_x)
    cur = [[0]*n,[0]*n]
    for i in range(n): cur[0][i] = val_y[i]
    ans = [cur[0][0]]
    for i in range(n-1):
        for j in range(n-i-1):
            cur[not (i&1)][j] = (cur[i&1][j+1]-cur[i&1][j])/(val_x[j+i+1]-val_x[j])
        ans.append(cur[not (i&1)][0])
    return ans

def findAnswer(x, val_x, val_y, limit):
    n = len(val_x)
    r = 0
    while r<n and val_x[r] < x: r += 1

    if r == n: return float('nan')
    if val_x[r] == x: return val_y[r]
    if r == 0: return float('nan')
    limit = min(limit,n)
    l = r-1
    while r-l+1 < limit:
        if l == 0 or (r != n-1 and x - val_x[l-1] > val_x[r+1] - x): r += 1
        else: l -= 1

    temp = L(x,val_x[l:r+1])

    res = 0
    for j in range(limit):
        res += temp[j]*val_y[l+j]

    return res

# p1 = [10,14,15,18,20,22,25,27,30]
# v1 = [60,55,52,47,46,44,43,42,40]
# p2 = [30,31,35,37,40]
# v2 = [40,35,30,25,20]
v1 = [22,25,27,30]
p1 = [44,43,42,40]
v2 = [30,31,35,37]
p2 = [40,35,30,25]
ans1 = findAnswer(28,v1,p1,4)
ans2 = findAnswer(28,v1,p1,3)
print("Volume at V= 28 m^3 is = ",ans1)

print("The absolute approximate relative error is = ",abs((ans1-ans2)/ans1)*100,'%')

ans1 = findAnswer(32,v2,p2,4)
ans2 = findAnswer(32,v2,p2,3)
print("Volume at V= 32 m^3 is = ",ans1)

print("The absolute approximate relative error is = ",abs((ans1-ans2)/ans1)*100,'%')

#graph plot
a = np.arange(10,30,0.05)
b = [findAnswer(x,v1,p1,4) for x in a]

plt.plot(a,b,color = 'blue')

a = np.arange(30,40,0.05)
b = [findAnswer(x,v2,p2,4) for x in a]


plt.plot(a,b,color = 'blue')
plt.plot(32,findAnswer(32,v2,p2,4),32,'o',color = 'green')
plt.plot(28,findAnswer(28,v1,p1,4),28,'o',color = 'red')
plt.show()


#INTEGRATION
# x = Symbol('X')
# f = L(x,p1)
#
# for i in range(4):
#     f[i] *= v1[i]
#
# f_prime = integrate(f)
# print(f)
# print(f_prime)
#
# f_prime = lambdify(x,f_prime)
# print(f_prime(1))

#INTEGRATION
x = Symbol('X')

d = f_newton(p1,v1)

f = d[0]
age = (x-p1[0])
for i in range(1,4):
    f += age*d[i]
    age *= (x-p1[i])

f_prime = integrate(f)
f_prime = lambdify(x,f_prime)

ans = f_prime(30)-f_prime(25)


d = f_newton(p2,v2)

f = d[0]
age = (x-p2[0])
for i in range(1,4):
    f += age*d[i]
    age *= (x-p2[i])

f_prime = integrate(f)
f_prime = lambdify(x,f_prime)
ans += f_prime(35)-f_prime(30)

print("W = ",ans)