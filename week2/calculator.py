class Calculator:
    def add(self, a, b):
        sum = a + b
        print(f'sumary of \t{a}, {b} equal to {sum}')

    def sub(self, a, b):
        sub = a - b
        print(f'subtraction of \t{a}, {b} equal to {sub}')

    def mul(self, a, b):
        mul = a * b
        print(f'multiple of \t{a}, {b} equal to {mul}')

    def div(self, a, b):
        div = a / b
        print(f'division of \t{a}, {b} equal to {div:.2f}')

cal1 = Calculator()

cal1.add(20,13)
cal1.sub(20,13)
cal1.mul(20,13)
cal1.div(20,13)