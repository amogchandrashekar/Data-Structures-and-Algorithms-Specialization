"""
Problem Description

Task. The goal in this code problem is to check whether an input sequence contains a majority element.
Input Format. The first line contains an integer n, the next one contains a sequence of n non-negative
integers a 0 , a 1 , . . . , a n−1 .
Constraints. 1 ≤ n ≤ 10 5 ; 0 ≤ a i ≤ 10 9 for all 0 ≤ i < n.
Output Format. Output 1 if the sequence contains an element that appears strictly more than n/2 times,
and 0 otherwise.

Sample 1.
Input:
5
23922
Output:
1
2 is the majority element.

Sample 2.
Input:
4
1234
Output:
0
There is no majority element in this sequence.

"""
# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    left_elem = get_majority_element(a, left, (left + right - 1) // 2 + 1)
    right_elem = get_majority_element(a, (left + right - 1) // 2 + 1, right)

    lcount = 0
    for i in range(left, right):
        if a[i] == left_elem:
            lcount += 1
    if lcount > (right - left) // 2:
        return left_elem

    rcount = 0
    for i in range(left, right):
        if a[i] == right_elem:
            rcount += 1
    if rcount > (right - left) // 2:
        return right_elem

    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
