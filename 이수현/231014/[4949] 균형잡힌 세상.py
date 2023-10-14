import sys


def is_balanced(ary):
    stack = []
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

    if len(stack) == 0:
        return "yes"
    else:
        return "no"


while True:
    word = input().rstrip()
    if word == ".":  # . 이 들어오면 종료
        break
    # word = input().strip()
    print(is_balanced(word))
