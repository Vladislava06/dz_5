def digit(a, b):
    if (b == 1):
        return (a)
    if (b != 1):
        return (a * digit(a, b - 1))
a = int(input("Введите число: "))
b = int(input("Введите его степень: "))
print("Результат равен:", digit(a, b))