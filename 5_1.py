my_f = open('test.txt', 'w', encoding='utf-8')
line = input('Введите текст или пустую строку для завершения \n')
while line:
    my_f.writelines(line)
    line = input('Введите текст или пустую строку для завершения \n')
    if not line:
        break

my_f.close()
my_f = open('test.txt', 'r')
content = my_f.readlines()
print(content)
my_f.close()