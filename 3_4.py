def my_func(x, y):
    num1 = x ** y
    num2 = 1
    i = 1
    while i <= abs(y):
        num2 *= x
        i += 1

    return num1, 1 / num2


print(my_func(int(input("Число 1: ")), int(input("Число 2 "))))
