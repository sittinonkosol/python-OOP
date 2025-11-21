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

a,b = map(int, input().split())

cal1.add(a,b)
cal1.sub(a,b)
cal1.mul(a,b)
cal1.div(a,b)