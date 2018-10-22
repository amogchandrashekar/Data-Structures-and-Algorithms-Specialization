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


