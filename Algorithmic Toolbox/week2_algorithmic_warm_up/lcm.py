"""

Problem Description
Task. Given two integers a and b, find their least common multiple.
Input Format. The two integers a and b are given in the same line separated by space.
Constraints. 1 ≤ a, b ≤ 2 · 10 9 .
Output Format. Output the least common multiple of a and b.

Sample 1.
Input:
68
Output:
24
Among all the positive integers that are divisible by both 6 and 8 (e.g., 48, 480, 24), 24 is the smallest
one.

Sample 2.
Input:
28851538 1183019
Output:
1933053046
1933053046 is the smallest positive integer divisible by both 28851538 and 1183019.

"""

# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

