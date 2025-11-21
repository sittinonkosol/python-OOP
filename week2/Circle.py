class Circle:
    def user_input(self):
        self.diameter = int(input('โปรดกรอกเส้นผ่าศูนย์กลาง : '))

    def cal_circle_ridius(self):
        self.radius = self.diameter / 2
        return self.radius

cal = Circle()

cal.user_input()

print(cal.cal_circle_ridius())
