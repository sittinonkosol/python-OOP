class Smartphone:
    manufacturer = "nig-ono"

    def __init__(self, model, storage, battery):
        self.model = model
        self.storage_gb = storage
        self.battery_percent = battery

    def battery_status(self):
        if self.battery_percent >= 80:
            batt_status = 'full'
        elif self.battery_percent >= 40:
            batt_status = 'medium'
        elif self.battery_percent > 0:
            batt_status = 'low'
        
        return batt_status
    
    @classmethod
    def show_brand(cls, new_brand):
        old_manufacturer = cls.manufacturer
        cls.manufacturer = new_brand
        return [old_manufacturer , cls.manufacturer]
    
    @staticmethod
    def calculate_warranty(price, years):
        if years > 3:
            rate = 0.02
        elif years in range(1,4):
            rate = 0.05
        elif years < 1:
            rate = 0.10
        
        return price * rate * years


nany_phone = Smartphone('ono phone 54 5G', 128, 37)
print('batter_status : ', nany_phone.battery_status())
brand_change = nany_phone.show_brand('nitore')
print(f'changed {brand_change[0]} -> {brand_change[1]}')
print('warranty_price : ', nany_phone.calculate_warranty(12990, 2))