# Class Attributes (Sınıf Özellikleri)
class Person:
    country = "USA"
    number_of_people = 0   # class attribute

    def __init__(self, name, age):
        self.name = name     # instance attribute
        self.age = age
        Person.number_of_people += 1   # Her yeni oluşturlan bir instance ile 1 artar
        self.id = Person.number_of_people


person1 = Person("Tim", 19)
person2 = Person("Jill", 20)

# Sınıf özelliğine örnek (instance) üzerinden erişilir.
print(person1.number_of_people)
print(person2.number_of_people)

# Sınıf özelliğine sınıf adı üzerinden erişilir.
print(Person.number_of_people)

# Sınıf özelliği dışarıdan değiştirilebilir
Person.number_of_people = 8

# Örnek özelliği güncellendiğinde sadece o örneğe ait olan özellik değişir.
person1.age = 21

# Örnek üzerinden bir sınıf özelliği güncellendiğinde, sınıf özelliği güncellenmez.
person1.country = "Turkey"
















