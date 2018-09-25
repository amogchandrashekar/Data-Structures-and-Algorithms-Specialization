# Uses python3
import sys

def inversion_by_merge_sort(a):
    """
    This function is used to find the inversions in a list such that a[i]>a[j] where i<j using the merge sort.
    The number of inversions in a list gives the amount by which the list is far from being sorted

    :param a: list from which the inversions have to be found out
    :return: sorted list (inplace) and the number of inversions in the list

    sample :
    >>> a =[2,3,9,2,9]
    >>> inversion_by_merge_sort(a)
    [2,2,3,9,9],2
    """

    if len(a)==1:
        return a,0

    mid = len(a)//2
    left,left_count_inversion = inversion_by_merge_sort(a[:mid])
    right,right_count_inversion = inversion_by_merge_sort(a[mid:])

    i = 0
    j = 0
    c=[]
    count_inversion = left_count_inversion+right_count_inversion

    while(i<len(left) and j<len(right)):
        if left[i]<right[j]:
            c.append(left[i])
            i+=1

        elif left[i]>right[j]:
            c.append(right[j])
            j+=1
            count_inversion += (len(left)-i)

        else:
            c.append(left[i])
            i+=1

    c += left[i:]
    c += right[j:]

    return c,count_inversion



if __name__ == '__main__':
    input = sys.stdin.read()
    a = list(map(int, input.split()))
    print(inversion_by_merge_sort(a)[-1])
