"""

Problem Description

Task. The goal in this code problem is to implement the binary search algorithm.
Input Format. The first line of the input contains an integer n and a sequence a 0 < a 1 < . . . < a n−1
of n pairwise distinct positive integers in increasing order. The next line contains an integer k and k
positive integers b 0 , b 1 , . . . , b k−1 .
Constraints. 1 ≤ n, k ≤ 10 4 ; 1 ≤ a i ≤ 10 9 for all 0 ≤ i < n; 1 ≤ b j ≤ 10 9 for all 0 ≤ j < k;
Output Format. For all i from 0 to k − 1, output an index 0 ≤ j ≤ n − 1 such that a j = b i or −1 if there
is no such index.

Sample 1.
Input:
5 1 5 8 12 13
5 8 1 23 1 11
Output:
2 0 -1 0 -1
In this sample, we are given an increasing sequence a 0 = 1, a 1 = 5, a 2 = 8, a 3 = 12, a 4 = 13 of length
five and five keys to search: 8, 1, 23, 1, 11. We see that a 2 = 8 and a 0 = 1, but the keys 23 and 11 do
not appear in the sequence a. For this reason, we output a sequence 2, 0, −1, 0, −1.

"""

# Uses python3
import sys

def binary_search_iterative(a, x):
    left, right = 0, len(a) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if a[mid] == x:
            return mid
        elif x < a[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1: n + 1]
    for x in data[n + 2:]:
        print(binary_search_iterative(a, x), end=' ')
