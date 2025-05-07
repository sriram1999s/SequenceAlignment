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

    x_l = x[:m//2]
    x_r = x[m//2:]

    print(x_l)
    print(x_r)
    print(y)

    # Divide 
    ix = OptSplitPoint(x_l, x_r, y)
    print(ix)
    # Conquer

    # Merge

def OptSplitPoint(x_l, x_r, y):

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

    m = len(y)
    n1 = len(x_l)
    
    ldp = [[0] * (n1 + 1) for _ in range(m+1)]

    for i in range(1, m+1):
        ldp[i][0] = i * delta
    
    for j in range(1, n1+1):
        ldp[0][j] = j * delta

    for i in range(1, m+1):
        for j in range(1, n1+1):
            ldp[i][j] = min(ldp[i-1][j-1] + misMatch[y[i-1] + x_l[j-1]],
                           ldp[i-1][j] + delta, 
                           ldp[i][j-1] + delta)
            

    
    x_r = x_r[::-1]
    y = y[::-1]

    n2 = len(x_r)
    rdp = [[0] * (n2 + 1) for _ in range(m+1)]

    for i in range(1, m+1):
        rdp[i][0] = i * delta
    
    for j in range(1, n2+1):
        rdp[0][j] = j * delta

    for i in range(1, m+1):
        for j in range(1, n2+1):
            rdp[i][j] = min(rdp[i-1][j-1] + misMatch[y[i-1] + x_r[j-1]],
                           rdp[i-1][j] + delta, 
                           rdp[i][j-1] + delta)
    

    ix = -1
    mi = float('inf')

    for i in range(m+1):
        inter = ldp[i][n1] + rdp[m - i][n2]

        if inter < mi:
            mi = inter 
            ix = i

    return ix


def main():
    x, y = InputGen(sys.argv[1])
    DivideAndConquer(x, y)

if __name__ == '__main__':
    main()