# Üst Sınıf: BasePhone. Constructor: phone_id, brand, model, price.
#                       Methods: show_information(), phone_ring_sound()
# Alt Sınıf: Samsung. Constructor: operating_system.
#                     Methods: show_information(), phone_ring_sound()

class BasePhone:
    def __init__(self, id, brand, model, price):
        self.id = id
        self.brand = brand
        self.model = model
        self.price = price

    def show_info(self):
        return f"ID: {self.id}\nBrand: {self.brand}\nModel: {self.model}\nPrice: {self.price}"

    def phone_ring_sound(self):
        print("Common ring sound!")


class Samsung(BasePhone):
    def __init__(self, id, brand, model, price, operating_system):
        super().__init__(id, brand, model, price)
        self.operating_system = operating_system

    def show_info(self):
        print(super().show_info(), f"\nOS: {self.operating_system}")

    def phone_ring_sound(self, sound):
        print(f"Phone ring sound: {sound}")


samsung1 = Samsung(1, "Samsung", "Note-2", 700, "Android")
samsung2 = Samsung(2, "Samsung", "S24", 800, "Android")

samsung1.show_info()
samsung2.show_info()

samsung1.phone_ring_sound("Four Seasons")
