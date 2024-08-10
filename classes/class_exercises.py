# Exercise-1 Create a Car class
# 2 adet özelliğe sahip (attributes) Car sınıfı oluşturun.
# .color, arabanın rengini string olarak saklasın
# .mileage, aracın kat ettiği mesafeyi int olarak saklasın
# 20.000 mil mavi araba, 30.000 mil kırmızı araba nesnesi oluşturun.
# color ve mileage özelliklerini yazdırın
# str metodu oluşturun  (The red car has 30000 miles)


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"The {self.color} car has {self.mileage} miles"


car1 = Car("blue", 20_000)
car2 = Car("red", 30_000)
car3 = Car("purple", 25_000)

print(car1)
print(car2)
print(car3)

for car in (car1, car2, car3):
    print(f"The {car.color} car has {car.mileage} miles")


for car in [car1, car2, car3]:
    print(car)


# Exercise 2 Create Dog class
# Dog sınıfı oluşturun, 2 arguman alsın: name, age
# str method ile description return edin.
# location isimli metod oluşturun, bu metod bir argüman alsın. "Miles lives in Ankara"
# set_age isimli bir metod oluşturun ve yaşını güncelleyin.  set_age(self, age)
# Buddy isimli bir instance oluşturun. Yaşı 5 olsun. Daha sonra yaşını 6 olarak güncelleyin.

class Dog:
    def __init__(self, name, age, city=None):
        self.name = name
        self.age = age
        self.city = city

    def __str__(self):
        if self.city is None:
            return f"{self.name}({self.age})"
        return f"{self.name}({self.age}), {self.city}"

    def add_location(self, new_city):
        self.city = new_city

    def location(self):
        return f"{self.name} lives in {self.city}"

    def set_age(self, new_age):
        self.age = new_age


buddy = Dog("Buddy", 5)
print(buddy)
buddy.add_location("Ankara")
print(buddy)
print(buddy.location())
buddy.set_age(6)
print(buddy)

