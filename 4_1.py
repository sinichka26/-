def salary():
    try:
        time = float(input('Выработка в часах = '))
        rate = int(input('Ставка =  '))
        bonus = int(input('Премия =  '))
        res = time * rate + bonus
        print(f'Заработная плата сотрудника  {res}')
    except ValueError:
        return print('Not a number')
salary()