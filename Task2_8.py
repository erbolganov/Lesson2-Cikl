# Найти максимальное из натуральных чисел, не превышающих 5000, которое нацело делится на 39.

n = 5000

while n % 39 != 0:
    n -= 1

print("Максимальное натуральное число, которое делится на 39: ", n)