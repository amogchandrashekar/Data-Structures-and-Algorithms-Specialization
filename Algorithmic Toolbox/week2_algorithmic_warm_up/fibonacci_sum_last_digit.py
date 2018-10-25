"""

Problem Description

Task. Given an integer n, find the last digit of the sum F 0 + F 1 + · · · + F n .
Input Format. The input consists of a single integer n.
Constraints. 0 ≤ n ≤ 10 18 .
Output Format. Output the last digit of F 0 + F 1 + · · · + F n .

Sample 1.
Input:
3
Output:
4
F 0 + F 1 + F 2 + F 3 = 0 + 1 + 1 + 2 = 4.

Sample 2.
Input:
100
Output:
5
The sum is equal to 927 372 692 193 078 999 175, the last digit is 5.

"""
# Uses python3
import sys

def get_fibonacci_last_digit_fast(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current % 10, (previous + current) % 10

    return current


def fibonacci_sum_fast(n):
    new_n = (n + 2) % 60
    new_last = get_fibonacci_last_digit_fast(new_n)
    if new_last == 0:
        return 9
    else:
        return new_last - 1

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    # n=100
    print(fibonacci_sum_fast(n))
