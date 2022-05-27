def my_func(word):
    latin_char = 'qwertyuioplkjhgfdsazxcvbnm'
    return word.title() if not set(word).difference(latin_char) else False


words = input("Введите слова через пробел: ").split()
for w in words:
    result = my_func(w)
    if result:
        print(result, '  ')
