'''
Problem : Compose the largest number out of a set of integers.
Input Format : The first line of the input contains an integer n. The second line contains integers
a 1 , a 2 , . . . , a n .
Constraints : 1 ≤ n ≤ 100; 1 ≤ a i ≤ 10 3 for all 1 ≤ i ≤ n.
Output Format : Output the largest number that can be composed out of a 1 , a 2 , . . . , a n .

Sample 1.
Input:
>>> 2
>>>21 2
Output:
221
'''
import sys

def isgreaterorequal(largest,number):
    '''
    Function that returns largest of the two combination of numbers
    :param largest: The current largest in the list
    :param number: The number to be compared with the largest
    :return: Boolean depending on if the number is greater than the largest(False) else True
    '''
    number1 = str(largest)[0]
    number2 = str(number)[0]
    if number1==number2:
        number1 = str(largest)+str(number)
        number2 = str(number)+str(largest)
    return number1>number2

def largest_number(a):
    """
    Driver Function
    :param a: List of numbers from which the largest possible number has to be made
    :return: The largest possible number from the list
    """
    res = ""
    while len(a)>0:
        largest = a[0]
        for number in a:
            if number!=largest:
                flag = isgreaterorequal(largest,number)
                if flag==False:
                    largest = number
        res+=str(largest)
        a.remove(largest)

    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
