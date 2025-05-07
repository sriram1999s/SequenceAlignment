import sys
from resource import *
import time
import psutil

def InputGen(fileName):
    base1 = ''
    j = 0
    lbase1 = 0

    base2 = ''
    k = 0
    lbase2 = 0
    
    isFirst = True
    isSecond = False

    with open(fileName, 'r') as file:
        for line in file:
            line  = line.strip()
            #print(line)
            if isFirst: # parsing base 1
                base1 = line
                isFirst = False
                lbase1 = len(base1)
            elif line.isdigit() and not isSecond: # parsing all j values
                j += 1
                ix = int(line)
                base1 = base1[:ix+1] + base1 + base1[ix+1:]
            elif line.isdigit(): # parsing all k values
                k += 1
                ix = int(line)
                base2 = base2[:ix+1] + base2 + base2[ix+1:]
            else: # parsing base 2
                base2 = line 
                isSecond = True
                lbase2 = len(base2)

    # validating length of strings 
    assert(len(base1) == 2**j * lbase1)
    assert(len(base2) == 2**k * lbase2)
    

    return (base1, base2)

def DivideAndConquer(x, y):
    m, n = len(x), len(y)

    if m == 0:
        return (n * delta, n * '_', y) 
    if n == 0:
        return (m * delta, x, m * '_')
    
    if m < 5 or n < 5:
        dp = [[0] * (n + 1) for _ in range(m+1)]

        for i in range(1, m+1):
            dp[i][0] = i * delta
        
        for j in range(1, n+1):
            dp[0][j] = j * delta

        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = min(dp[i-1][j-1] + misMatch[x[i-1] + y[j-1]],
                            dp[i-1][j] + delta, 
                            dp[i][j-1] + delta)
        
        OPT = dp[m][n]

        rx = ''
        ry = ''

        while m>0 and n>0:
            
            if dp[m][n] == dp[m-1][n-1] + misMatch[x[m-1] + y[n-1]]:
                rx = x[m-1] + rx
                ry = y[n-1] + ry
                m-=1
                n-=1
            elif dp[m][n] == dp[m][n-1] + delta:
                rx = '_' + rx
                ry =  y[n-1] + ry
                n-=1
            else:
                rx = x[m-1] + rx
                ry = '_' + ry
                m-=1
        
        while m>0:
            rx = x[m-1] + rx
            ry = '_' + ry
            m-=1
        while n>0:
            rx = '_' + rx
            ry =  y[n-1] + ry
            n-=1

        return (OPT, rx, ry)
    
    
    x_l = x[:m//2]
    x_r = x[m//2:]

    # print(x_l)
    # print(x_r)
    # print(y)

    # Divide 
    ix = OptSplitPoint(x_l, x_r, y)
    # print(ix)
    # Conquer
    y_l = y[:ix]
    y_r = y[ix:]
    lval, lresx, lresy = DivideAndConquer(x_l, y_l)
    rval, rresx, rresy = DivideAndConquer(x_r, y_r)

    # Merge
    return (lval+rval, lresx + rresx, lresy + rresy)

def OptSplitPoint(x_l, x_r, y):

    m = len(y)
    n1 = len(x_l)
    
    ldp = [[0] * (2) for _ in range(m+1)]

    for i in range(1, m+1):
        ldp[i][0] = i * delta

    for j in range(1, n1+1):
        ldp[0][1] = j * delta
        for i in range(1, m+1):
            ldp[i][1] = min(ldp[i-1][0] + misMatch[y[i-1] + x_l[j-1]],
                           ldp[i-1][1] + delta, 
                           ldp[i][0] + delta)
        for i in range(0, m+1):
            ldp[i][0] = ldp[i][1]

    
    x_r = x_r[::-1]
    y = y[::-1]

    n2 = len(x_r)
    rdp = [[0] * (2) for _ in range(m+1)]

    for i in range(1, m+1):
        rdp[i][0] = i * delta

    for j in range(1, n2+1):
        rdp[0][1] = j * delta
        for i in range(1, m+1):
            rdp[i][1] = min(rdp[i-1][0] + misMatch[y[i-1] + x_r[j-1]],
                           rdp[i-1][1] + delta, 
                           rdp[i][0] + delta)
        for i in range(0, m+1):
            rdp[i][0] = rdp[i][1]
    

    ix = -1
    mi = float('inf')

    for i in range(m+1):
        inter = ldp[i][1] + rdp[m - i][1]

        if inter < mi:
            mi = inter 
            ix = i

    return ix


def main():
    x, y = InputGen(sys.argv[1])
    val, x, y = DivideAndConquer(x, y)
    print(val)
    print(x)
    print(y)

if __name__ == '__main__':
    # all mismatch values
    misMatch = {}
    misMatch['AA'] = 0
    misMatch['GG'] = 0
    misMatch['CC'] = 0
    misMatch['TT'] = 0
    misMatch['AC'] = misMatch['CA'] = 110
    misMatch['AG'] = misMatch['GA'] = 48
    misMatch['AT'] = misMatch['TA'] = 94
    misMatch['CG'] = misMatch['GC'] = 118
    misMatch['CT'] = misMatch['TC'] = 48
    misMatch['GT'] = misMatch['TG'] = 110

    # delta
    delta = 30
    main()