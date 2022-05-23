my_str = input("Введите несколько слов через пробел: ").split()
for s, i in enumerate(my_str, 1):
    print(f'{s}. {i:.10}')