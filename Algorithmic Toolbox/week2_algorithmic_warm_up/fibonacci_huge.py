"""

Problem Description
Task. Given two integers n and m, output F n mod m (that is, the remainder of F n when divided by m).
Input Format. The input consists of two integers n and m given on the same line (separated by a space).
Constraints. 1 ≤ n ≤ 10 18 , 2 ≤ m ≤ 10 3 .
Output Format. Output F n mod m.

Sample 1.
Input:
239 1000
Output:
161
F 239 mod 1 000 = 39 679 027 332 006 820 581 608 740 953 902 289 877 834 488 152 161 (mod 1 000) = 161.

Sample 2.
Input:
2816213588 239
Output:
151
F 2 816 213 588 does not fit into one page of this file, but F 2 816 213 588 mod 239 = 151.

"""

# Uses python3
import sys

def get_fibonacci(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current

def fib_period_length(m):
    previous = 0
    current = 1
    for i in range(m * m + 1):
        previous, current = current, (previous + current) % m
        if previous == 0 and current == 1:
            return i + 1


def get_fibonacci_huge_fast(n, m):
    remainder = n % fib_period_length(m)
    return get_fibonacci(remainder) % m


if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge_fast(n, m))
