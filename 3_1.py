def div(arg1, arg2):
    try:
        arg1, arg2 = int(arg1), int(arg2)
        div_num = arg1 / arg2
    except ValueError:
        return ("Value Error")
    except ZeroDivisionError:
        return ("Zero Division Error - нельзя делить на ноль!")
    return round(div_num, 4)


print(div(input("Введите первое число: "), input("Введите второе число: ")))
