p, m = map(int, input().split())
s = input().strip()

hash_value = 0
power = 1

for character in s:
    character_value = ord(character) - ord("a") + 1
    hash_value = (hash_value + character_value * power) % m
    power = power * p % m

print(hash_value)