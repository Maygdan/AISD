a = float(input())
n = int(input())

exponent = abs(n)
result = 1.0

while exponent > 0:
    if exponent % 2 == 1:
        result *= a
    a *= a
    exponent //= 2

if n < 0:
    result = 1 / result

print(format(result, ".15g"))