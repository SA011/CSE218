import numpy as np
import matplotlib.pyplot as plt

def printstep(A, B):
    for x in A:
        for y in x:
            print(round(y, 4), end=' ')
        print()
    for x in B:
        print(round(x[0], 4))


def gaussianElimination(A, B, d=False):
    valid = []  # variables which can have unique solution
    n = np.shape(A)[0]
    j = 0
    for i in range(n):
        # step 1 for column i
        # here row is j (i==j only if there is unique solution)

        if A[j][i] == 0:
            k = j + 1
            while k < n:
                if A[k][i] != 0:
                    break
                k += 1
            if k == n:
                # Every value is 0. There is no unique solution for it
                continue
            A[[j, k]] = A[[k, j]]
            B[[j, k]] = B[[k, j]]
        valid.append(j)

        k = j + 1
        while k < n:
            mul = A[k][i] / A[j][i]
            for l in range(i, n):
                A[k][l] -= A[j][l] * mul
            B[k]-= B[j] * mul
            k += 1

        if d:
            print("Working with row no: " + str(j))
            printstep(A, B)
            print()
        j += 1

    ans = np.zeros((n, 1))

    # if len(valid)!=n then either there is infinitely many solution or no solution at all
    # if len(valid) == n then there is unique solution

    for i in range(len(valid) - 1, -1, -1):
        val = B[i]
        for j in range(valid[i] + 1, n):
            val -= ans[j][0] * A[i][j]
        ans[valid[i]][0] = val / A[i][valid[i]]

    nosol = False
    for i in range(n):
        val = 0.0
        for j in range(n):
            val += ans[j] * A[i][j]
        if abs(val - B[i]) > 1e-9:
            nosol = True
            break

    if nosol:
        print("There is no solution")
        return

    if len(valid) != n:
        print("There is infinitely many solution")
        return ans

    return ans

def dataCollection():
    file = open("in.txt", "r")
    data = []
    for str in file:
        data.append(list(map(float,str.strip().split())))
    return np.array(data)

def polynomialRegression(data, m):
    n = len(data)
    pw = [0.0]*(2*m+1)
    p = []
    for i in range(n):
        cur = 1.0
        p.append([])
        for j in range(2*m+1):
            pw[j] += cur
            p[i].append(cur)
            cur *= data[i][0]

    A = np.zeros((m+1, m+1))
    B = np.zeros(m+1)

    for i in range(m+1):
        for j in range(m+1):
            A[i][j] = pw[i+j]
        for j in range(n):
            B[i] += p[j][i] * data[j][1]

    return gaussianElimination(A, B)

def dataPlotting(data):
    x = np.reshape(data[:,0],(-1))
    y = np.reshape(data[:,1],(-1))
    plt.scatter(x, y,color = 'Red')

def f(val, x):
    return 1.0/(val[0] + val[1]*(1.0/(x*x)))

def curvePlotting(val, l, r, num):
    x = np.arange(l,r,(r-l)/num)
    y = np.array([f(val, i) for i in x])
    plt.plot(x,y)

if __name__ == '__main__':
    data = dataCollection()
    dataPlotting(data)
    for i in data:
        i[0] = 1.0/(i[0]*i[0])
        i[1] = 1.0/(i[1])
    curve = polynomialRegression(data,1)
    print("Kmax = ", 1.0/curve[0])
    print("Cs = ", curve[1]/curve[0])
    curvePlotting(curve,0.01,5,2000)
    plt.xlabel('C')
    plt.ylabel('K')
    plt.show()
