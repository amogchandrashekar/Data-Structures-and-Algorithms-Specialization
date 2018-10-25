"""
Problem Description

Task. Given two integers a and b, find their greatest common divisor.
Input Format. The two integers a, b are given in the same line separated by space.
Constraints. 1 ≤ a, b ≤ 2 · 10 9 .
Output Format. Output GCD(a, b).

Sample 1.
Input:
18 35
Output:
1
18 and 35 do not have common non-trivial divisors.

Sample 2.
Input:
28851538 1183019
Output:
17657
28851538 = 17657 · 1634, 1183019 = 17657 · 67.

"""
# Uses python3
import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
