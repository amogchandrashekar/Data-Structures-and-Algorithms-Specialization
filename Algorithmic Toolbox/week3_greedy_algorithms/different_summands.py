"""

Problem Description

Task. Given a set of n segments {[a 0 , b 0 ], [a 1 , b 1 ], . . . , [a n−1 , b n−1 ]} with integer coordinates on a line, find
the minimum number m of points such that each segment contains at least one point. That is, find a
set of integers X of the minimum size such that for any segment [a i , b i ] there is a point x ∈ X such
that a i ≤ x ≤ b i .
Input Format. The first line of the input contains the number n of segments. Each of the following n lines
contains two integers a i and b i (separated by a space) defining the coordinates of endpoints of the i-th
segment.
Constraints. 1 ≤ n ≤ 100; 0 ≤ a i ≤ b i ≤ 10 9 for all 0 ≤ i < n.
Output Format. Output the minimum number m of points on the first line and the integer coordinates
of m points (separated by spaces) on the second line. You can output the points in any order. If there
are many such sets of points, you can output any set. (It is not difficult to see that there always exist
a set of points of the minimum size such that all the coordinates of the points are integers.)

Sample 1.
Input:
3
13
25
36
Output:
1
3
In this sample, we have three segments: [1, 3], [2, 5], [3, 6] (of length 2, 3, 3 respectively). All of them
contain the point with coordinate 3: 1 ≤ 3 ≤ 3, 2 ≤ 3 ≤ 5, 3 ≤ 3 ≤ 6.

"""

# Uses python3
import sys


def optimal_summands(n):
    summands = []
    for i in range(1, n + 1):
        n -= i
        if n <= i:
            summands.append(n + i)
            break
        elif n == 0:
            summands.append(i)
            break
        else:
            summands.append(i)
    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
