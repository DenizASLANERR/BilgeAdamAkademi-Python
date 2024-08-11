####### MULTIPLE INHERITANCE #######
# Ata sınıf: Creature, constructor oluşturun, isim (name) adında bir argüman alsın.
# 2 metodu olsun. attack(), defence() pass

# FlyingCreature adında bir alt sınıf oluşturun. Creature'dan inheritance alsın.
# fly() metodu tanımlayın. "isim" uçuyor çıktısı versin.

# AquaticCreature adında bir alt sınıf oluşturun. Creature'dan inheritance alsın.
# swim() metodu tanımlayın. "isim" yüzüyor çıktısı versin.

# Dragon adında bir alt sınıf oluşturun. FlyingCreature, AquaticCreature sınıflarından miras alsın.
# Constructor oluşturun. Yeni özellik olarak color ekleyin.
# attack() ve defence() metodlarını override edin.
# isim ateş püskürterek saldırıyor
# isim kanatlarıyla kendini savunuyor.

class Creature:
    def __init__(self, name):
        self.name = name

    def attack(self):
        pass

    def defence(self):
        pass


class FlyingCreature(Creature):
    def fly(self):
        print(f"{self.name} uçuyor")


class AquaticCreature(Creature):
    def swim(self):
        print(f"{self.name} yüzüyor")


class Dragon(FlyingCreature, AquaticCreature):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def attack(self):
        print(f"{self.name} ateş püskürterek saldırıyor")

    def defence(self):
        print(f"{self.name} kanatlarıyla kendini savunuyor")

    def fly(self):
        print(f"{self.color} rengindeki {self.name} hızlı uçuyor")


dragon1 = Dragon("Ejderya", "gri")

dragon1.fly()
dragon1.attack()
dragon1.defence()
dragon1.swim()

print(isinstance(dragon1, Dragon))
print(isinstance(dragon1, AquaticCreature))
print(isinstance(dragon1, Creature))

print(issubclass(Dragon, Creature))
