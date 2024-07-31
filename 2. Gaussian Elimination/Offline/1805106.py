import numpy as np

def printStep(A,B):
    for x in A:
        for y in x:
            print(round(y,4),end=' ')
        print()
    for x in B:
        print(round(x[0],4))
def GaussianElimination(A,B,d = True):
    valid = []      #variables which can have unique solution
    n = np.shape(A)[0]
    j = 0
    for i in range(n):
        #step 1 for column i
        #here row is j (i==j only if there is unique solution)

        if A[j][i] == 0:
            k = j+1
            while k<n:
                if A[k][i]!=0:
                    break
                k+=1
            if k==n:
                #Every value is 0. There is no unique solution for it
                continue
            A[[j,k]] = A[[k,j]]
            B[[j,k]] = B[[k,j]]
        valid.append(j)

        k = j+1
        while k<n:
            mul = A[k][i]/A[j][i]
            for l in range(i,n):
                A[k][l] -= A[j][l]*mul
            B[k][0] -= B[j][0]*mul
            k+=1

        if d:
            print("Working with row no: "+str(j))
            printStep(A,B)
            print()
        j+=1

    ans = np.zeros((n,1))

    #if len(valid)!=n then either there is infinitely many solution or no solution at all
    #if len(valid) == n then there is unique solution

    for i in range(len(valid)-1,-1,-1):
        val = B[i][0]
        for j in range(valid[i]+1,n):
            val-=ans[j][0]*A[i][j]
        ans[valid[i]][0] = val/A[i][valid[i]]

    nosol = False
    for i in range(n):
        val = 0.0
        for j in range(n):
            val+=ans[j]*A[i][j]
        if abs(val-B[i][0])>1e-9:
            nosol = True
            break

    if nosol:
        print("There is no solution")
        return

    if len(valid) != n:
        print("There is infinitely many solution")
        return ans

    return ans



n = int(input("Number of variables: "))

a = []
b = []
for i in range(n):
    a.append(list(map(float,input().split())))

for i in range(n):
        b.append(float(input()))

A = np.array(a,dtype=float)
B = np.array(b,dtype=float)
B = B.reshape((n,1))
sol = GaussianElimination(A,B)
if type(sol) != type(None):
    print("\nRESULT:")
    for x in sol:
        print(round(x[0],4))
