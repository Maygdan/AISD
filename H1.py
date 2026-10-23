a, n, m = map(int, input().split())

old_remainder, remainder = m, a % m
old_coefficient, coefficient = 0, 1

while remainder:
    quotient = old_remainder // remainder
    old_remainder, remainder = remainder, old_remainder - quotient * remainder
    old_coefficient, coefficient = (
        coefficient,
        old_coefficient - quotient * coefficient,
    )

if old_remainder != 1:
    print(-1)
else:
    inverse = old_coefficient % m
    inverse_power = 1
    answer = 0

    for i in range(1, n + 1):
        inverse_power = inverse_power * inverse % m
        answer = (answer + i * inverse_power) % m

    print(answer)