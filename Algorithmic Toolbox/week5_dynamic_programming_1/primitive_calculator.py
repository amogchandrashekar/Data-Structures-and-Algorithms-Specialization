"""
Primitive Calculator

Problem Description
Task. Given an integer n, compute the minimum number of operations needed to obtain the number n
starting from the number 1.
Input Format. The input consists of a single integer 1 ≤ n ≤ 10 6 .
Output Format. In the first line, output the minimum number k of operations needed to get n from 1.
In the second line output a sequence of intermediate numbers. That is, the second line should contain
positive integers a 0 , a 2 , . . . , a k−1 such that a 0 = 1, a k−1 = n and for all 0 ≤ i < k − 1, a i+1 is equal to
either a i + 1, 2a i , or 3a i . If there are many such sequences, output any one of them.

Sample 1.
Input:
1
Output:
0
1

Sample 2.
Input:
5
Output:
3
1245
Here, we first multiply 1 by 2 two times and then add 1. Another possibility is to first multiply by 3
and then add 1 two times. Hence “1 3 4 5” is also a valid output in this case.

Sample 3.
Input:
96234
Output:
14
1 3 9 10 11 22 66 198 594 1782 5346 16038 16039 32078 96234
Again, another valid output in this case is “1 3 9 10 11 33 99 297 891 2673 8019 16038 16039 48117
96234”.
"""

# Uses python3
import sys

def optimal_sequence(n):
    if n == 1:
        return [1]
    ops = min_ops(n)
    return construct_min_list(n, ops)

def construct_min_list(n, ops):
    result = []
    while(n>=1):
        result.append(n)
        if n%3 != 0 and n%2 != 0:
            n -= 1

        elif n%3 == 0 and n%2 == 0:
            n = int(n/3)

        elif n%3 == 0:
            if ops[n-1] < ops[n//3]:
                n = n-1
            else:
                n = n // 3

        elif n%2 == 0:
            if ops[n-1] < ops[n//2]:
                n = n-1
            else:
                n = n // 2

    return reversed(result)

def min_ops(n):
    result = [0 for i in range(n+1)]
    for i in range(2,n+1):
        min_1 = result[i-1]
        min_2 = sys.maxsize
        min_3 = sys.maxsize

        if i%2 == 0:
            min_2 = result[int(i//2)]

        if i%3 == 0:
            min_3 = result[int(i//3)]

        minOperations = min(min_1,min_2,min_3)+1
        result[i] = minOperations

    return result

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
