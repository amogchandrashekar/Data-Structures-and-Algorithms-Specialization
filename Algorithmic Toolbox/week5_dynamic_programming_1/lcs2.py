#Uses python3

"""
Problem Introduction
Compute the length of a longest common subsequence of three sequences.

Problem Description
Task. Given two sequences A = (a 1 , a 2 , . . . , a n ) and B = (b 1 , b 2 , . . . , b m ), find the length of their longest
common subsequence, i.e., the largest non-negative integer p such that there exist indices 1 ≤ i 1 <
i 2 < · · · < i p ≤ n and 1 ≤ j 1 < j 2 < · · · < j p ≤ m, such that a i 1 = b j 1 , . . . , a i p = b j p .

Input Format. First line: n. Second line: a 1 , a 2 , . . . , a n . Third line: m. Fourth line: b 1 , b 2 , . . . , b m .
Constraints. 1 ≤ n, m ≤ 100; −10 9 < a i , b i < 10 9 .
Output Format. Output p.

Sample 1.
Input:
3
275
2
25
Output:
2
A common subsequence of length 2 is (2, 5).

Sample 2.
Input:
1
7
4
1234
Output:
0
The two sequences do not share elements.

Sample 3.
Input:
4
2783
4
5287
Output:
2
One common subsequence is (2, 7). Another one is (2, 8).
"""

import sys

def lcs2(a, b):
    #write your code here
    m = len(a)
    n = len(b)

    L = [[None] * (n + 1) for x in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif a[i - 1] == b[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    return L[i][j]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
