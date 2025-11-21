class Student:
    university = 'UBU'

    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def grade(self):
        if self.score >= 80: return 'A'
        if self.score >= 70: return 'B'
        if self.score >= 60: return 'C'
        if self.score >= 50: return 'D'
        if self.score < 49: return 'F'
    
    @classmethod
    def change_university(cls, new_university):
        old_university = cls.university
        cls.university = new_university
        return (old_university, cls.university)

    @staticmethod
    def is_pass(score):
        return score >= 50

stu_data = ('shitthinon', 26)
shitthinon_oop = Student(name=stu_data[0], score=stu_data[1])
print('grade \t\t: ', shitthinon_oop.grade())
university_change = shitthinon_oop.change_university('TSMGO')
print('changed \t: ', university_change[0], '->', university_change[1])
print('ispass? \t: ', shitthinon_oop.is_pass(stu_data[1]))