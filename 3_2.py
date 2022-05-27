def personal_info(**kwargs):
    return ", ".join(kwargs.values())


name = input("Введите свое имя: ")
surname = input("Введите свою фамилию: ")
birthday = input("Введите свою дату рождения: ")
city = input("Введите город проживания: ")
email = input("Введите свой email: ")
telephone = input("Введите свой телефон: ")

print(personal_info(n=name, s=surname, b=birthday, c=city, e=email, t=telephone))
