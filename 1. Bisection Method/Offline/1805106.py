import pandas as pd
import matplotlib.pyplot as plt


pt,K = 3,0.05

def f(x):
    if abs(x-1)<1e-7 or abs(2+x)<1e-7:
        return float('NaN')
    return x/(1-x)*((2*pt/(2+x))**0.5)-K

def plotGraph(start,end,gap):
    x = []
    y = []
    it = start
    while it<end:
        x.append(it)
        y.append(f(it))
        it += gap

    plt.plot(x,y,linewidth = 2)
    plt.grid(True)

    plt.xlabel("X")
    plt.ylabel("F(X)")

    plt.show()

def findRoot(lowerBound, upperBound, relativeError, maxIter):
    root = lowerBound
    lvalue = f(lowerBound)
    rvalue = f(upperBound)

    if lvalue*rvalue>0:
        return


    for i in range(maxIter):
        newRoot = (lowerBound+upperBound)/2
        newValue = f(newRoot)

        if newValue == 0:
            return newRoot
        if i!=0:
            curError = abs((root-newRoot)/newRoot*100)
            if curError<relativeError:
                return newRoot


        if lvalue*newValue<0:
            rvalue = newValue
            upperBound = newRoot
        else:
            lvalue = newValue
            lowerBound = newRoot
        root = newRoot

    return root


def showTable(lowerBound,upperBound,relativeError,maxIter):
    root = lowerBound
    lvalue = f(lowerBound)
    rvalue = f(upperBound)

    if lvalue * rvalue > 0:
        return

    table = {'Lower Bound':[],'Upper Bound':[],'Root':[],' Relative Error(%)':[]}

    for i in range(maxIter):
        newRoot = (lowerBound + upperBound) / 2
        newValue = f(newRoot)

        table['Upper Bound'].append(upperBound)
        table['Lower Bound'].append(lowerBound)
        table['Root'].append(newRoot)
        if i != 0:
            curError = abs((root - newRoot) / newRoot * 100)
            table[' Relative Error(%)'].append(curError)
        else:
            table[' Relative Error(%)'].append('nan')

        if lvalue * newValue < 0:
            rvalue = newValue
            upperBound = newRoot
        else:
            lvalue = newValue
            lowerBound = newRoot
        root = newRoot

    res = pd.DataFrame(table)
    res.index +=1
    print(res)


plotGraph(-2,5,0.1)

lb,ub = -0.8,0.8

print("Root: "+str(findRoot(lb,ub,0.05,100)))
print()

showTable(lb,ub,0.0001,20)