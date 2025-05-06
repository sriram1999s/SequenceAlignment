import sys

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
            print(line)
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
            
if __name__ == '__main__':
    string1, string2 = InputGen(sys.argv[1])

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

    m = len(string1)
    n = len(string2)

    dp = [[0] * (n + 1) for _ in range(m+1)]

    for i in range(1, m+1):
        dp[i][0] = i * delta
    
    for j in range(1, n+1):
        dp[0][j] = j * delta

    for i in range(1, m+1):
        for j in range(1, n+1):
            dp[i][j] = min(dp[i-1][j-1] + misMatch[string1[i-1] + string2[j-1]],
                           dp[i-1][j] + delta, 
                           dp[i][j-1] + delta)
            
    OPT = dp[m][n]

    