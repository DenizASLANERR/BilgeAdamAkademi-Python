# classmethod, hem sınıfın kendisine hem de tüm örneklerine erişim sağlayan
# bir metot türüdür. Bu tür metotlar genelde sınıfın durumunu değiştirmek veya sınıf
# seviyesindeki verilere erişmek için kullanılır.

class Person:
    number_of_people = 0     # class attribute (sınıf özelliği)
    person_list = []

    def __init__(self, name):
        self.name = name
        Person.add_person(self.name)     # Her yeni nesne oluşturulduğunda kişi sayısını artırır.

    @classmethod
    def num_of_people(cls):
        """Bu classmethod, sınıfın kaç tane örneği olduğunu döndürür"""
        return cls.number_of_people

    @classmethod
    def add_person(cls, name):
        """Bu classmethod, bir kişi eklendiğinde number_of_people değerini artırır"""
        cls.number_of_people += 1
        cls.person_list.append(name)

    def person_info(self):
        return f"My name is {self.name}"


p1 = Person("Oguzhan")
p2 = Person("Deniz")
p3 = Person("Yunus")

# Sınıf özellği ve metoduna hem sınıf adı hem de örnekler üzerinden erişilebilir
print(Person.number_of_people)
print(Person.num_of_people())

print(Person.person_list)

p1.number_of_people
p2.num_of_people()

# Ancak, sınıf adı üzerinden bir örnek metoduna erişilemez.
try:
    Person.person_info()
except TypeError as e:
    print(f"Error: {e}")


from datetime import datetime

timestamp = 1723881755

dt_object = datetime.fromtimestamp(timestamp)
print(dt_object)

