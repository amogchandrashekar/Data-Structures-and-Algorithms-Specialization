"""
Money Change Again

As we already know, a natural greedy strategy for the change problem does not work correctly for any set of
denominations. For example, if the available denominations are 1, 3, and 4, the greedy algorithm will change
6 cents using three coins (4 + 1 + 1) while it can be changed using just two coins (3 + 3). Your goal now is
to apply dynamic programming for solving the Money Change Problem for denominations 1, 3, and 4.
Problem Description

Input Format. Integer money.
Output Format. The minimum number of coins with denominations 1, 3, 4 that changes money.
Constraints. 1 ≤ money ≤ 10 3 .

Sample 1.
Input:
2
Output:
2
2 = 1 + 1.

Sample 2.
Input:
34
Output:
9
34 = 3 + 3 + 4 + 4 + 4 + 4 + 4 + 4 + 4.
"""

# Uses python3
import sys

def get_change(target,coins,coins_sum):
    if target==0:
        return 0

    if target in coins_sum:
        return coins_sum[target]

    minimum=99999999

    for coin in coins:
        if target>=coin:
            a=minimum
            b=get_change(target-coin,coins,coins_sum)
            numberOfCoins = 1 + min(a,b)

            coins_sum[target]=numberOfCoins

            if (numberOfCoins < minimum):
                minimum = numberOfCoins
    return minimum

if __name__ == '__main__':
    m = int(sys.stdin.read())
    coins = [1,3,4]
    coins_sum = {}
    print(get_change(m,coins,coins_sum))
