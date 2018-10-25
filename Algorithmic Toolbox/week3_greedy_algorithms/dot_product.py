"""

Problem Description

Task. Given two sequences a 1 , a 2 , . . . , a n (a i is the profit per click of the i-th ad) and b 1 , b 2 , . . . , b n (b i is
the average number of clicks per day of the i-th slot), we need to partition them into n pairs (a i , b j )
such that the sum of their products is maximized.
Input Format. The first line contains an integer n, the second one contains a sequence of integers
a 1 , a 2 , . . . , a n , the third one contains a sequence of integers b 1 , b 2 , . . . , b n .
Constraints. 1 ≤ n ≤ 10 3 ; −10 5 ≤ a i , b i ≤ 10 5 for all 1 ≤ i ≤ n.
Output Format. Output the maximum value of
n
∑︀
a i c i , where c 1 , c 2 , . . . , c n is a permutation of
i=1
b 1 , b 2 , . . . , b n .

Sample 1.
Input:
1
23
39
Output:
897
897 = 23 · 39.

Sample 2.
Input:
3
1 3 -5
-2 4 1
Output:
23
23 = 3 · 4 + 1 · 1 + (−5) · (−2).
"""

#Uses python3

import sys


def max_dot_product(a, b):
    a.sort()
    b.sort()

    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
