import sys
input = sys.stdin.readline

N, M = map(int, input().split())

pokemon = {}

for i in range(1, 1 + N):
    pokemon_name = input().strip()
    pokemon[i] = pokemon_name
    pokemon[pokemon_name] = i

for i in range(M):
    quest = input().strip()
    if quest.isdigit():
        print(pokemon[int(quest)])
    else:
        print(pokemon
        [quest])

