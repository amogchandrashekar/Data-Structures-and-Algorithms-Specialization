"""
Problem Description

Task. Given an integer n, find the nth Fibonacci number F n .
Input Format. The input consists of a single integer n.
Constraints. 0 ≤ n ≤ 45.
Output Format. Output F n .

Sample 1.
Input:
10
Output:
55
F 10 = 55.

"""
def calc_fib(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current


n = int(input())
print(calc_fib(n))
