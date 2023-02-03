# Вывести на экран ряд натуральных чисел от минимума до максимума с шагом. Например, если минимум 10,
# максимум 35, шаг 5, то вывод должен быть таким: 10 15 20 25 30 35.
# Минимум, максимум и шаг указываются пользователем (считываются с клавиатуры).


while True:
    First = int(input(" Enter 1st number:  "))
    Second = int(input(" Enter 2nd number:  "))
    step = int(input(" Enter step:  "))
    if First <= Second and step <= Second - First:

        First += step
    elif First >= Second and step <= First - Second:

print(First)