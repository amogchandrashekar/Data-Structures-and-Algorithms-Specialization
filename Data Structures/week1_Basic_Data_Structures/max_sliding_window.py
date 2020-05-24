# python3
import collections


def max_sliding_window_naive(nums, k):
    ans = []
    deque = collections.deque()
    for i in range(len(nums)):
        if deque and deque[0] <= i - k:
            deque.popleft()
        while deque and nums[deque[-1]] <= nums[i]:
            deque.pop()
        deque.append(i)
        if i >= k - 1:
            ans.append(nums[deque[0]])
    return ans


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(" ".join(map(str, max_sliding_window_naive(input_sequence, window_size))))
