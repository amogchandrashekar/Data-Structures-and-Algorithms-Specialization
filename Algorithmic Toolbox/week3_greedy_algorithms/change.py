"""

Problem Description
Task. The goal in this problem is to find the minimum number of coins needed to change the input value
(an integer) into coins with denominations 1, 5, and 10.
Input Format. The input consists of a single integer m.
Constraints. 1 ≤ m ≤ 10 3 .
Output Format. Output the minimum number of coins with denominations 1, 5, 10 that changes m.

Sample 1.
Input:
2
Output:
2
2 = 1 + 1.

Sample 2.
Input:
28
Output:
6
28 = 10 + 10 + 5 + 1 + 1 + 1.

"""


import sys

def get_change(m):
    '''
    Greedy implementation of rendering the change.
    This function returns the minimum number of coins needed to change the input value (an integer) into coins with denominations 1, 5, and 10.

    :param m: input value (an integer).
    :return: minimum number of coins needed to change the input value (an integer) into coins with denominations 1, 5, and 10.

    example :

    >>> m = 28
    6
    explaination : 28 = 10 + 10 + 5 + 1 + 1 + 1.
    '''
    denomination_tens = m // 10
    denomination_five = (m-(denomination_tens*10)) // 5
    denomination_one = m-(denomination_tens*10)-(denomination_five*5)
    return denomination_tens+denomination_five+denomination_one

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
