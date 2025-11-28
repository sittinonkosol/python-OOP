class Circle:
    def user_input(self):
        self.diameter = int(input('โปรดกรอกเส้นผ่าศูนย์กลาง : '))

    def cal_circle_ridius(self):
        import math
        self.circum = self.diameter * math.pi
        return "{:.2f}".format(self.circum)

cal = Circle()

cal.user_input()

print(cal.cal_circle_ridius())
