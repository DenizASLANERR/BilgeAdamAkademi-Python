#INHERITANCE (KALITIM, MİRAS)
# Eğer yazdığınız sınıf bir başka sınıfın özelleşmiş bir versiyonu ise kalıtım kullanabilirsiniz.
# Bu alt sınıf (child class), üst sınıfın (parent class) özellik ve metotlarını miras alır.

# Üst Sınıf (Parent Class)
# Pet sınıfı, tüm evcil hayvanların temel özelliklerini temsil eder.

class Pet:
    def __init__(self, name, age):    # Constructor (Yapıcı) Method
        self.name = name
        self.age = age

    # Evcil hayvanların bilgilerini gösteren metot
    def show(self):     # Instance (Örnek) method
        print(f'I am {self.name} and I am {self.age} years old.')

    # Konuşma yeteneği ile ilgili bir metot
    def speak(self):
        print("I don't know what to say")


# Örnek (Instance) Oluşturmak
pet = Pet("Max", 4)
print(pet.name, pet.age)
pet.show()
pet.speak()


# Alt Sınıf (Child Class)
# Cat sınıfı, Pet sınıfından türetilecek (derived)
# Cat sınıfı, Pet sınıfından miras (inheritance) alacak.

class Cat(Pet):
    def color(self, color):
        print(f"I am a Cat. My color is {color}")


daisy = Cat("Daisy", 2)
print(daisy.name, daisy.age)

cat2 = Cat()  # TypeError: Pet.__init__() missing 2 required positional arguments: 'name' and 'age'

daisy.color("white")   # Cat sınıfına ait bir metot
daisy.show()           # Pet sınıfından miras gelen bir metot
daisy.speak()          # Pet sınıfından miras gelen bir metot

