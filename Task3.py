# Даны два целых числа A и В. Выведите все числа от A до B включительно, в порядке возрастания, если A < B,
# или в порядке убывания в противном случае.
# входные данные
# 5 9
# выходные данные
# 5 6 7 8 9

A = int(input("Enter 1st number:  "))
B = int(input("Enter 2nd number:  "))
if A > B:

    while A >= B:
        print(A)
        A -= 1
elif B > A:
    while A <= B:
        print(A)
        A += 1
