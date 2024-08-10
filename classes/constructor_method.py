# Yapıcı (Constructor) Metot
# __init() metodu, özel metottur (special method)

class Dog:
    x = "abc"                           # Sınıfa Ait özellik
    def __init__(self, name, age):      # Yapıcı Metot (Constructor Method)
        self.name = name                # Örnek Özelliği (Instance Attribute)
        self.age = age                  # Örnek Özelliği (Instance Attribute)

    def description(self):              # Örnek Metot (Instance Method)
        return f"{self.name} is {self.age} years old."

    def speak(self, sound):             # Örnek Metot (Instance Method) w/arguments
        return f"{self.name} says {sound}"


# Örnek Oluşturmak / Örnekleme (Instantiation)
dog1 = Dog()                            # TypeError: Dog.__init__() missing 2 required positional arguments: 'name' and 'age'
dog1 = Dog("Miles", 5)
dog2 = Dog("Mars", 7)
dog3 = Dog("Diablo", 3)

# Örnek Özelliklerine Erişmek
print(dog1.name)
print(dog1.age)
print(dog2.name)
print(dog2.age)
print(dog3.name)
print(dog3.age)

print(Dog.name)                         # AttributeError: type object 'Dog' has no attribute 'name'
print(Dog.x)

# Örnek (Instance) Metodlarına erişme
dog2.speak("woof")
print(dog2.description())
print(dog3.description())


# Şuana kadar öğrendiğimiz konseptler
# Sınıf Oluşturmak
# Sınıfın yapıcı (Constructor) Metodu Oluşturmak
# Örnek Özellikleri (Instance Attributes)
# Örnek Metodları (Instance Methods)

# Dog sınıfını Geliştirleim.

class Dog:
    def __init__(self, name, age, weight=None):
        self.name = name
        self.age = age
        self.weight = weight
        self.health_records = []

    def change_weight(self, weight):
        self.weight = weight

    def __str__(self):                  # __str__() özel metodu nesnenin resmi olmayan temsilini verir. print() ile çalışır
        if self.weight is None:
            return f"{self.name}({self.age})"
        return f"{self.name}({self.age}), {self.weight}kg"

# mars isminde Dog sınıfından türetilmiş bir nesne oluşturalım.
mars = Dog("Mars", 8)

# print() fonksiyonu ile __str__() özel metodunun döndürdüğü ifadeyi yazdıralım.
print(mars)

# change_weight() örnek metodunu kullanarak örnek özelliği olan self.weight'i değiştirelim.
mars.change_weight(25)
print(mars)

# Resmi olmayana methot user, resmi olan methost reaper devoloeper olarak geçer


# self.health_records isimli örnek özelliği nesnenin sağlık kayıtlarını tutmaktadır.
# En başta boş olan bu listeyi dolduralım.
mars.health_records.append("Right leg is broken")
mars.health_records.append("A bruise in the neck")

print(mars.health_records)

miles = Dog("Miles", 7)

miles.health_records.append("Severe wound")

fiora = Dog("Fiora", 11, 27)
print(fiora)
fiora.__str__()