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
