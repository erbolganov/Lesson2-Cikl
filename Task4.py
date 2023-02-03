# Вывести на экран ряд натуральных чисел от минимума до максимума с шагом. Например, если минимум 10,
# максимум 35, шаг 5, то вывод должен быть таким: 10 15 20 25 30 35.
# Минимум, максимум и шаг указываются пользователем (считываются с клавиатуры).

First = int(input(" Enter 1st number:  "))
Second = int(input(" Enter 2nd number:  "))
step = int(input(" Enter step:  "))
if step <= Second - First or step <= First - Second:
    if First <= Second:
        print(First)
        while step <= Second - First:
            First += step
            print(First)
        print(Second)
    elif First >= Second:
        print(First)
        while step <= First - Second:
            First -= step
            print(First)
        print(Second)
else:
    print(f'There are no any numbers between {First} and {Second} with this step')
    print(First, Second)