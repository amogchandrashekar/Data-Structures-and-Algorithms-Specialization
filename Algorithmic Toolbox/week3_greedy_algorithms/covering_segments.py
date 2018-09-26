'''
Problem :

Task : Given a set of n segments {[a 0 , b 0 ], [a 1 , b 1 ], . . . , [a n−1 , b n−1 ]} with integer coordinates on a line, find
the minimum number m of points such that each segment contains at least one point. That is, find a
set of integers X of the minimum size such that for any segment [a i , b i ] there is a point x ∈ X such
that a i ≤ x ≤ b i.

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

'''
import sys
from collections import namedtuple

Segment = namedtuple('Segment', ['start','end'])

def find_smallest_endpoint(segments):
    '''
    Function to find the smallest endpoint among the segments
    :param segments: list of namedtuples of various segments
    :return minimum: smallest endpoint among the segments
    '''
    minimum = segments[0].end
    for segment in segments:
        if segment.end < minimum:
            minimum = segment.end
    return minimum

def remove_segments_in_range(segments,remove_segment):
    '''
    Function to remove the segments which are in a particular range
    :param segments: list of namedtuples of various segments
    :param remove_segment: list of namedtuples to remove from segments
    :return segments: list of namedtuples of various segments
    '''
    for segment in remove_segment:
        segments.remove(segment)
    return segments

def optimal_points(segments):
    '''
    Driver function
    :param segments: list of namedtuples of various segments
    :return count_segments: list of points of seperate segments
    '''
    count_segments = []
    while len(segments)>0:
        smallest_point = find_smallest_endpoint(segments)
        remove_segment = []
        count_segments.append(smallest_point)
        for segment in segments:
            if smallest_point<=segment.end and smallest_point>=segment.start:
                remove_segment.append(segment)
        segments = remove_segments_in_range(segments,remove_segment)
    return count_segments

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
