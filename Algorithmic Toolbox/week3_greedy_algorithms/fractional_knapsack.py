"""

Problem Description

Task. The goal of this code problem is to implement an algorithm for the fractional knapsack problem.
Input Format. The first line of the input contains the number n of items and the capacity W of a knapsack.
The next n lines define the values and weights of the items. The i-th line contains integers v i and w i —the
value and the weight of i-th item, respectively.
Constraints. 1 ≤ n ≤ 10 3 , 0 ≤ W ≤ 2 · 10 6 ; 0 ≤ v i ≤ 2 · 10 6 , 0 < w i ≤ 2 · 10 6 for all 1 ≤ i ≤ n. All the
numbers are integers.
Output Format. Output the maximal value of fractions of items that fit into the knapsack. The absolute
value of the difference between the answer of your program and the optimal value should be at most
10 −3 . To ensure this, output your answer with at least four digits after the decimal point (otherwise
your answer, while being computed correctly, can turn out to be wrong because of rounding issues).

Sample 1.
Input:
3 50
60 20
100 50
120 30
Output:
180.0000
To achieve the value 180, we take the first item and the third item into the bag.

Sample 2.
Input:
1 10
500 30
Output:
166.6667
Here, we just take one third of the only available item.

"""

# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0.
    proportion = [float(v) / float(w) for v, w in zip(values, weights)]
    for _ in range(len(weights) + 1):
        if capacity == 0:
            return value
        max_weight = max(proportion)
        index = proportion.index(max_weight)
        proportion[index] = -1
        add_capacity = min(capacity, weights[index])
        value += add_capacity * max_weight
        weights[index] -= add_capacity
        capacity -= add_capacity
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))