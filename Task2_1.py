# Имеется фрагмент программы в виде оператора цикла с параметром, обеспечивающий вывод на экран
# «столбиком» всех целых чисел от 10 до 30. Оформить этот фрагмент в виде:
# а) оператора цикла с предусловием;
# б) оператора цикла с постусловием.

num1 = n = 10
num2 = 30

print("а) оператора цикла с предусловием: ")
while n <= num2:
    print(n)
    n += 1

print("---------------------------------------\n")

print("б) оператора цикла с постусловием: ")
while True:
    print(num1)
    num1 += 1
    if num1 > num2:
        break

