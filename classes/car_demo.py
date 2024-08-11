# CLASS ATTRIBUTE DEMO
# Bir Car sınıfı oluşturalım. Constructor'ında make, model alsın.
# add_fuel(self, amount) isimli bir instance method. Bu arabanın fuel (yakıt) verisini güncellesin.
# drive(self, distance). Yeteri kadar yakıt varsa bu mesafeyi kat etsin ve fuel özelliğini güncellesin (azalsın).
# Araçlar 1 litre benzin ile 20 km mesafe katediyorlar
# Araç filosu oluşturacağız (3 adet Car örneği).
# Alınan toplam yakıt (total_fuel_bought) ve harcanan toplam yakıt (total_fuel_consumed). Class Attribute

class Car:
    number_of_cars = 0    # class attribute
    total_fuel_consumed = 0  # toplam harcanan
    total_fuel_bought = 0   # toplam satın alınan

    def __init__(self, make, model):     # constructor method
        self.make = make
        self.model = model
        self.fuel = 0
        self.odometer = 0   # km sayacı
        Car.number_of_cars += 1

    def add_fuel(self, amount):
        self.fuel += amount    # örnek özelliği güncellendi
        Car.total_fuel_bought += amount # sınıf özelliği güncellendi
        print(f"Adding {amount} lt fuel. Now fuel: {self.fuel}.")

    def drive(self, distance):
        fuel_needed = distance * 0.05
        if self.fuel >= fuel_needed:
            self.odometer += distance
            self.fuel -= fuel_needed
            Car.total_fuel_consumed += fuel_needed
            print(f"{self.make} {self.model} drove {distance} kilometers and comsumed {fuel_needed} litre(s).")
        else:
            print(f"Not enough fuel to drive {distance} kilometer(s). You need to buy {fuel_needed - self.fuel} liter(s).")


car1 = Car("Renault", "Toros")
car2 = Car("Toyota", "Camry")
car3 = Car("Porsche", "Taycan")
car4 = Car("Volvo", "XC90")


car1.drive(10)
car1.add_fuel(2)
car2.add_fuel(2)
car3.add_fuel(3)

car1.drive(10)
car2.drive(40)
car3.drive(100)
car3.drive(50)
car3.drive(10)
car3.add_fuel(0.5)
car3.drive(10)
