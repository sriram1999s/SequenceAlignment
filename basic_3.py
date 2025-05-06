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
            
def main():
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

    rstring1 = ''
    rstring2 = ''

    while m>0 and n>0:
        
        if dp[m][n] == dp[m-1][n-1] + misMatch[string1[m-1] + string2[n-1]]:
            rstring1 = string1[m-1] + rstring1
            rstring2 = string2[n-1] + rstring2
            m-=1
            n-=1
        elif dp[m][n] == dp[m][n-1] + delta:
            rstring1 = '_' + rstring1
            rstring2 =  string2[n-1] + rstring2
            n-=1
        else:
            rstring1 = string1[m-1] + rstring1
            rstring2 = '_' + rstring2
            m-=1
    
    while m>0:
        rstring1 = string1[m-1] + rstring1
        rstring2 = '_' + rstring2
        m-=1
    while n>0:
        rstring1 = '_' + rstring1
        rstring2 =  string2[n-1] + rstring2
        n-=1

    # print(OPT)
    # print(rstring1)
    # print(rstring2)

    with open(sys.argv[2], 'w') as f:
        f.write(str(OPT) + '\n')
        f.write(str(rstring1) + '\n')
        f.write(str(rstring2) + '\n')

def process_memory () :
    process = psutil . Process ()
    memory_info = process . memory_info ()
    memory_consumed = int ( memory_info . rss /1024)
    return memory_consumed

def time_wrapper () :
    start_time = time . time ()
    main () # Replace with your algorithm function call
    end_time = time . time ()
    time_taken = ( end_time - start_time ) *1000
    return time_taken

if __name__ == '__main__':
    tim = time_wrapper()
    mem = process_memory()
    # print(tim)
    # print(mem)
    with open(sys.argv[2], 'a') as f:
        f.write(str(tim) + '\n')
        f.write(str(mem) + '\n')