"""
Problem Description

Input Format. The first line contains an integer n. The second line contains integers v 1 , v 2 , . . . , v n separated
by spaces.
Constraints. 1 ≤ n ≤ 20, 1 ≤ v i ≤ 30 for all i.
Output Format. Output 1, if it possible to partition v 1 , v 2 , . . . , v n into three subsets with equal sums, and
0 otherwise.

Sample 1.
Input:
4
3333
Output:
0

Sample 2.
Input:
1
40
Output:
0

Sample 3.
Input:
11
17 59 34 57 17 23 67 1 18 2 59
Output:
1
34 + 67 + 17 = 23 + 59 + 1 + 17 + 18 = 59 + 2 + 57.

Sample 4.
Input:
13
1 2 3 4 5 5 7 7 8 10 12 19 25
Output:
1
1 + 3 + 7 + 25 = 2 + 4 + 5 + 7 + 8 + 10 = 5 + 12 + 19.

"""
# Uses python3
import sys


def subsetsum(A,n,sum_1,sum_2,sum_3,lookup):

    if sum_1==0 and sum_2==0 and sum_3==0:
        return True

    if n<0:
        return False

    key = str(sum_1)+'|'+str(sum_2)+'|'+str(sum_3)+'|'+str(n)

    if key not in lookup:

        flag_a = False
        if sum_1-A[n]>=0:
            flag_a = subsetsum(A,n-1,sum_1-A[n],sum_2,sum_3,lookup)

        flag_b = False
        if flag_a==False and sum_2-A[n]>=0:
            flag_b = subsetsum(A, n - 1, sum_1, sum_2 - A[n], sum_3, lookup)

        flag_c = False
        if flag_a == False and flag_b == False and sum_3 - A[n] >= 0:
            flag_c = subsetsum(A, n - 1, sum_1, sum_2, sum_3 - A[n], lookup)

        lookup[key] = flag_a or flag_b or flag_c

    return lookup[key]


def partition3(A):

    if len(A)<3:
        return 0

    lookup = {}
    sum_ = sum(A)

    answer =  sum_%3==0 and subsetsum(A,len(A)-1,int(sum_/3),int(sum_/3),int(sum_/3),lookup)

    if answer==True:
        return 1
    else:
        return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    # A = [3,3,3]
    print(partition3(A))
