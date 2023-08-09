import sys
input = sys.stdin.readline

word = input()

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet = list(range(97, 123))

for i in alphabet:
    print(word.find(chr(i)), end=" ")