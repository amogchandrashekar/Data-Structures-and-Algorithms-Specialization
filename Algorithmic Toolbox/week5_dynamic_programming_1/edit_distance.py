"""
Edit Distance

Problem Introduction
The edit distance between two strings is the minimum number of operations (insertions, deletions, and
substitutions of symbols) to transform one string into another. It is a measure of similarity of two strings.
Edit distance has applications, for example, in computational biology, natural language processing, and spell
checking. Your goal in this problem is to compute the edit distance between two strings.

Problem Description
Task. The goal of this problem is to implement the algorithm for computing the edit distance between two
strings.

Input Format. Each of the two lines of the input contains a string consisting of lower case latin letters.
Constraints. The length of both strings is at least 1 and at most 100.
Output Format. Output the edit distance between the given two strings.

Sample 1.
Input:
ab
ab
Output:
0

Sample 2.
Input:
short
ports
Output:
3

An alignment of total cost 3:
s h o r t −
− p o r t s

Sample 3.
Input:
editing
distance
Output:
5
An alignment of total cost 5:
e d i − t i n g −
− d i s t a n c e

"""

# Uses python3
def edit_distance(s, t):
    dp_result = [[x for x in range(len(s) + 1)] for y in range(len(t) + 1)]
    for y in range(len(t) + 1):
        dp_result[y][0] = y

    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            insert_op = dp_result[j-1][i] + 1
            delete_op = dp_result[j][i-1] + 1
            match_op = dp_result[j-1][i-1]
            mismatch_op = dp_result[j-1][i-1] + 1
            if s[i-1] == t[j-1]:
                dp_result[j][i] = min(insert_op, delete_op, match_op)
            else:
                dp_result[j][i] = min(insert_op, delete_op, mismatch_op)

    return dp_result[len(t)][len(s)]

if __name__ == "__main__":
    print(edit_distance(input(), input()))


