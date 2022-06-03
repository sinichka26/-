def text_3():
    wages = {}
    try:
        with open('text_3.txt', 'r', encoding='utf-8') as file:
            for line in file:
                wages[line.split()[0]] = float(line.split()[1])
        print('Оклад меньше 20.000 получают: ')
    for name, wage in wages.items():
        if wage < 20000:
            print(name)
    print(f'Средняя зп {sum(wages.values()) / len(wages)}')
    except IOError:
        print("Ошибка")
    except:
    print("Ошибка")


text_3()