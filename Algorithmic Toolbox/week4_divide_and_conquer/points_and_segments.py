"""

Problem Description

Task. You are given a set of points on a line and a set of segments on a line. The goal is to compute, for
each point, the number of segments that contain this point.

Input Format. The first line contains two non-negative integers s and p defining the number of segments
and the number of points on a line, respectively. The next s lines contain two integers a i , b i defining
the i-th segment [a i , b i ]. The next line contains p integers defining points x 1 , x 2 , . . . , x p .
Constraints. 1 ≤ s, p ≤ 50000; −10 8 ≤ a i ≤ b i ≤ 10 8 for all 0 ≤ i < s; −10 8 ≤ x j ≤ 10 8 for all 0 ≤ j < p.
Output Format. Output p non-negative integers k 0 , k 1 , . . . , k p−1 where k i is the number of segments which
contain x i . More formally,
k i = |{j : a j ≤ x i ≤ b j }| .

Sample 1.
Input:
23
05
7 10
1 6 11
Output:
100
Here, we have two segments and three points. The first point lies only in the first segment while the
remaining two points are outside of all the given segments.

Sample 2.
Input:
13
-10 10
-100 100 0
Output:
001

"""

# Uses python3
import sys
from itertools import chain

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    start_points = zip(starts, ['l'] * len(starts), range(len(starts)))
    end_points = zip(ends, ['r'] * len(ends), range(len(ends)))
    point_points = zip(points, ['p'] * len(points), range(len(points)))

    sort_list = chain(start_points, end_points, point_points)
    sort_list = sorted(sort_list, key=lambda a: (a[0], a[1]))
    segment = 0
    i = 0
    for num, letter, index in sort_list:
        if letter == 'l':
            segment += 1
        elif letter == 'r':
            segment -= 1
        else:
            cnt[index] = segment
            i += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    # starts=[100,-5,7,120]
    # ends=[110,10,20,121]
    # points=[1000,2,3,4,7,8]
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
