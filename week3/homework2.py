class Beverage:
    def __init__(self, name, size, base_price):
        self.bev_name = name
        self._size =  size
        self.__base_price = base_price

    @property
    def size(self):
        return self._size
    
    @property
    def base_price(self):
        return self.__base_price
    
    @size.setter
    def size(self, value):
        value = value.strip().upper()
        if value in ['S', 'M', 'L']:
            self._size = value
        else:
            print('กรอกค่าไม่ถูกต้อง ค่าจะไม่เปลี่ยน')

    @base_price.setter
    def base_price(self, value):
        if value > 0:
            self.__base_price = value
    
    def calculate_price(self):
        self.start_price = self.base_price
        if self.size.upper() == "L":
            self.base_price += 20
        elif self.size.upper() == "M":
            self.base_price += 10
    
    def __str__(self):
        return f'Beverage(name={self.bev_name}, size={self.size}, price={self.base_price})'

class Coffee(Beverage):
    def __init__(self, name, size, base_price, extra_shot=0):
        super().__init__(name, size, base_price)
        self.extra_shot = extra_shot

    def calculate_price(self):
        super().calculate_price()
        self.base_price += self.extra_shot * 10

    def __str__(self):
        return f'Coffee(name={self.bev_name}, size={self.size}, extra_shot={self.extra_shot}, price={self.base_price})'
    
class Tea(Beverage):
    def __init__(self, name, size, base_price, sweet_level=0):
        super().__init__(name, size, base_price)
        self.sweet_level = sweet_level
    
    def calculate_price(self):
        super().calculate_price()
        if self.sweet_level == 0:
            self.base_price -= 5
    
    def __str__(self):
        return f'Tea(name={self.bev_name}, size={self.size}, sweet_level={self.sweet_level}, price={self.base_price})'
    
# ทดลองใช้งาน (main)
if __name__ == "__main__":
    b1 = Coffee("Latte", "M", 50, extra_shot=1)
    b2 = Coffee("Americano", "L", 45, extra_shot=0)
    b3 = Tea("Green Tea", "S", 40, sweet_level=0)

    menu = [b1, b2, b3]
    for drink in menu:
        print(drink)  # ใช้ __str__
        print(f"{drink.bev_name} ({drink.size}) price = {drink.calculate_price()}")
        print("-" * 40)
