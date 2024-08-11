class Mammal:
    def __init__(self, name):
        self.name = name

    def mammal_info(self):
        print("Memeliler doğum yapabilir.")


class WingedAnimal:
    def winged_animal_info(self):
        print("Kanatlı hayvanlar uçabilir.")


class Bat(Mammal, WingedAnimal):
    def bat_info(self):
        print("Yarasalar kanatlı memelilerdir.")


bat1 = Bat("Bat1")
print(type(bat1))

bat1.bat_info()
bat1.mammal_info()
bat1.winged_animal_info()

# isinstance()
isinstance(bat1, Mammal)
isinstance(bat1, WingedAnimal)
isinstance(bat1, Bat)

# issublass()
issubclass(Bat, Mammal)
issubclass(Bat, Bat)
issubclass(Bat, WingedAnimal)
issubclass(Bat, (Mammal, WingedAnimal, Bat))






