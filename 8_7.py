class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.n = 'a + b'

    def __add__(self, other):
        print(f'Сумма n1 и n2 равна')
        return f'n = {self.a + other.a} + {self.b + other.b}'

    def __mul__(self, other):
        print(f'Произведение n1 и n2 равно')
        return f'n = {self.a * other.a - (self.b * other.b)} * {self.b * other.a}'

    def __str__(self):
        return f'n = {self.a} * {self.b}'


n_1 = ComplexNumber(1, -2)
n_2 = ComplexNumber(3, 4)
print(n_1)
print(n_1+n_2)
print(n_1*n_2)