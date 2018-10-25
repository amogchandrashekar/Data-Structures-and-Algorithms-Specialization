"""
Problem Description

Task. Given an integer n, find the last digit of the nth Fibonacci number F n (that is, F n mod 10).
Input Format. The input consists of a single integer n.
Constraints. 0 ≤ n ≤ 10 7 .
Output Format. Output the last digit of F n .

Sample 1.
Input:
3
Output:
2
F 3 = 2.

Sample 2.
Input:
331
Output:
9
F 331 = 668 996 615 388 005 031 531 000 081 241 745 415 306 766 517 246 774 551 964 595 292 186 469

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

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_fast(n))
