# Напечатать минимальное число, большее 200, которое нацело делится на 17.

n = 200

while n % 17 != 0:
    n += 1
print("минимальное число, которое нацело делится на 17: ", n)
