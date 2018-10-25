"""

Problem Description
Task. Given n gold bars, find the maximum weight of gold that fits into a bag of capacity W .

Input Format. The first line of the input contains the capacity W of a knapsack and the number n of bars
of gold. The next line contains n integers w 0 , w 1 , . . . , w n−1 defining the weights of the bars of gold.
Constraints. 1 ≤ W ≤ 10 4 ; 1 ≤ n ≤ 300; 0 ≤ w 0 , . . . , w n−1 ≤ 10 5 .
Output Format. Output the maximum weight of gold that fits into a knapsack of capacity W .

Sample 1.
Input:
10 3
148
Output:
9
Here, the sum of the weights of the first and the last bar is equal to 9.

"""


# Uses python3
import sys

def optimal_weight(W, w):
    n = len(w)
    value = [[0 for x in range(W + 1)] for y in range(n + 1)]

    for i in range(1, n+1):
        for weight in range(1, W+1):
            value[i][weight] = value[i-1][weight]
            if w[i-1] <= weight:
                val = value[i-1][weight - w[i-1]] + w[i-1]
                if val > value[i][weight]:
                    value[i][weight] = val

    return value[n][W]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    # W = 10
    # w = [3 ,5 ,3 ,3 ,5]
    print(optimal_weight(W, w))
