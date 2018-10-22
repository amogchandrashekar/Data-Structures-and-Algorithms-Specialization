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