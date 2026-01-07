import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * math.pi * self.radius

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b

class Smartphone:
    # Class variabl
    manufacturer = "Unknown"

    def __init__(self, model, storage, battery):
        self.model = model
        self.storage = storage  # GB
        self.battery = battery  # %

    def battery_status(self):
        if self.battery >= 80:
            return "FULL"
        elif self.battery >= 40:
            return "MEDIUM"
        elif self.battery > 0:
            return "LOW"
        else:
            return "EMPTY"

    @classmethod
    def show_brand(cls, brand_name):
        cls.manufacturer = brand_name
        print(f"Brand set to: {cls.manufacturer}")

    @staticmethod
    def calculate_warranty(price, years):
        if years > 3:
            rate = 0.02
        elif years >= 1:
            rate = 0.05
        else:
            rate = 0.10
        
        return price * rate * years

class Student:
    # Class variable
    university = "UBU"

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def grade(self):
        if self.score >= 80:
            return "A"
        elif self.score >= 70:
            return "B"
        elif self.score >= 60:
            return "C"
        elif self.score >= 50:
            return "D"
        else:
            return "F"

    @classmethod
    def change_university(cls, new_university):
        cls.university = new_university

    @staticmethod
    def is_pass(score):
        return score >= 50

# Example usage
if __name__ == "__main__":
    print("--- วงกลม (Circle) ---")
    c = Circle(10)
    print(f"เส้นรอบวง (รัศมี=10): {c.circumference():.2f}")

    print("\n--- หนังสือ (Book) ---")
    b = Book("Harry Potter", "J.K. Rowling")
    print(f"หนังสือ: {b.title} เขียนโดย {b.author}")

    print("\n--- เครื่องคิดเลข (Calculator) ---")
    calc = Calculator()
    print(f"10 + 5 = {calc.add(10, 5)}")
    print(f"10 / 2 = {calc.divide(10, 2)}")

    print("\n--- สมาร์ทโฟน (Smartphone) ---")
    Smartphone.show_brand("Samsung")
    phone = Smartphone("Galaxy S24", 256, 85)
    print(f"รุ่น: {phone.model}, ความจุ: {phone.storage}GB")
    print(f"ผู้ผลิต: {phone.manufacturer}")
    print(f"สถานะแบตเตอรี่: {phone.battery_status()}")
    warranty_cost = Smartphone.calculate_warranty(30000, 2)
    print(f"ค่าประกัน (2 ปี, ราคา 30000): {warranty_cost:.2f}")

    print("\n--- นักเรียน (Student) ---")
    s1 = Student("John", 75)
    print(f"นักเรียน: {s1.name}, มหาวิทยาลัย: {s1.university}")
    print(f"คะแนน: {s1.score}, เกรด: {s1.grade()}")
    print(f"สอบผ่านหรือไม่ (75): {Student.is_pass(s1.score)}")

    Student.change_university("Chula")
    print(f"มหาวิทยาลัยใหม่ (Class Variable): {Student.university}")
    print(f"มหาวิทยาลัยของนักเรียนคนนี้ (Instance Access): {s1.university}")
