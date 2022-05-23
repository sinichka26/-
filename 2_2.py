number = int(input("Введите количество элементов списка "))
my_list = []
a = 0
b = 0
while a < number:
    my_list.append(input("Введите следующее значение списка "))
    a += 1

for elem in range(int(len(my_list)/2)):
        my_list[b], my_list[b + 1] = my_list [b + 1], my_list[b]
        b += 2
print(my_list)