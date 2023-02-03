#Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

number = int(input('Enter the number: '))
p = 0
n1 = 0
n2 = 0
while number > 0:
    p = number % 10
    if p % 2 == 0:
        n2 += 1
    else: n1 += 1
    number = number // 10
print(f'Taq sanlar {n1} ')
print(f'Jup sanlar {n2} ')