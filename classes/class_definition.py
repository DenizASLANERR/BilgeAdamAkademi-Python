mylist = list(range(3))

type(mylist)
mylist.append(3)


### SINIF (CLASS) OLUŞTURMAK ###

# Dog isminde bir sınıf oluşturalım.

class Dog:
    # Özellik (Attributes)
    name = "Mars"
    age = 5

    # Metotlar (Methods)
    def bark(self):               # Instance Method (Örnek Metodu)
        print("Dog is barking")

    def run(self):
        print("Dog is running")

    def eat(self, food):
        print("Dog is eating {}".format(food))

print(Dog)
print(type(Dog))    # <class 'type'>

### ÖRNEK (INSTANCE) OLUŞTURMAK --> ÖRNEKLEME (INSTANTIATION)  ###
dog1 = Dog()
dog2 = Dog()

print(dog1)
print(type(dog1))   # <class '__main__.Dog'>

# Özellikleri (Attributes) Çağırmak
print(f"Dog1's name is {dog1.name}\nDog1's age is {dog1.age}")
print(f"Dog2's name is {dog2.name}\nDog2's age is {dog2.age}")

dog2.name = "Saturn"

# Metotları (Mathods) Çağırmak
dog1.bark()
dog2.bark()

dog1.run()

dog1.eat("meat")
dog2.eat("bone")

# Sınıfı geliştirelim

class Dog:
    # Özellik (Attributes)
    name = "Mars"
    age = 5

    # Metotlar (Methods)
    def bark(self):               # Instance Method (Örnek Metodu)
        print(f"{self.name} is barking")

    def run(self):
        print("Dog is running")

    def eat(self, food):
        print("Dog is eating {}".format(food))

    @classmethod
    def sleep(cls):
        print("Dog is sleeping")


dog1 = Dog()
dog2 = Dog()
dog3 = Dog()

# Instance (Örnek) üzerinden metotlara erişim
dog1.bark()   # Instance method
dog1.sleep()  # Class method

# Class (Sınıf) üzerinden mettotlara erişim
Dog.name
Dog.bark()  # TypeError: Dog.bark() missing 1 required positional argument: 'self'
Dog.sleep()   # TypeError: Dog.sleep() missing 1 required positional argument: 'cls'



