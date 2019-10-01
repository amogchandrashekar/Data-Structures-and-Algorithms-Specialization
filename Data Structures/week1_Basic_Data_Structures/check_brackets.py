# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    stack = list()
    for i, next in enumerate(text):
        if next in "([{":
            stack.append(next)

        if next in ")]}":
            if stack:
                element = stack.pop()
            else:
                return -1
            if not are_matching(element, next):
                return -1

    if len(stack) == 0:
        return "Success"
    else:
        return -1


def main():
    text = input()
    print(find_mismatch(text))


if __name__ == "__main__":
    main()
