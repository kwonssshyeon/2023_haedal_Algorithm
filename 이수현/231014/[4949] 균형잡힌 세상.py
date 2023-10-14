import sys


def is_balanced(ary):
    stack = []
    if ary == ".":
        return "yes"

    for char in ary:
        if char in "([":
            stack.append(char)
        elif char in ")]":
            if not stack:
                return "no"
            if (char == ")" and stack[-1] == "(") or (char == "]" and stack[-1] == "["):
                stack.pop()
            else:
                return "no"

    if not stack:
        return "yes"
    else:
        return "no"


while True:
    try:
        ary = input().strip()
        if ary == ".":
            break
        print(is_balanced(ary))
    except EOFError:
        break
