#Uses python3

"""
Problem Introduction
Compute the length of a longest common subsequence of three sequences.

Problem Description
Task. Given three sequences A = (a 1 , a 2 , . . . , a n ), B = (b 1 , b 2 , . . . , b m ), and C = (c 1 , c 2 , . . . , c l ), find the
length of their longest common subsequence, i.e., the largest non-negative integer p such that there
exist indices 1 ≤ i 1 < i 2 < · · · < i p ≤ n, 1 ≤ j 1 < j 2 < · · · < j p ≤ m, 1 ≤ k 1 < k 2 < · · · < k p ≤ l such
that a i 1 = b j 1 = c k 1 , . . . , a i p = b j p = c k p

Input Format. First line: n. Second line: a 1 , a 2 , . . . , a n . Third line: m. Fourth line: b 1 , b 2 , . . . , b m . Fifth line:
l. Sixth line: c 1 , c 2 , . . . , c l .
Constraints. 1 ≤ n, m, l ≤ 100; −10 9 < a i , b i , c i < 10 9 .
Output Format. Output p.

Sample 1.
Input:
3
123
3
213
3
135
Output:
2
A common subsequence of length 2 is (1, 3).

Sample 2.
Input:
5
83217
7
8 2 1 3 8 10 7
6
683147
Output:
3
One common subsequence of length 3 in this case is (8, 3, 7). Another one is (8, 1, 7).
"""

import sys

def lcs3(a, b, c):
    x = len(a)
    y = len(b)
    z = len(c)

    L = [[[None]*(z+1) for j in range(y+1)] for k in range(x+1)]

    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i==0 or j==0 or k==0:
                    L[i][j][k] = 0

                elif a[i-1]==b[j-1] and b[j-1]==c[k-1]:
                    L[i][j][k] = 1+L[i-1][j-1][k-1]

                else:
                    L[i][j][k] = max(L[i-1][j][k],L[i][j-1][k],L[i][j][k-1])
    return L[i][j][k]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
