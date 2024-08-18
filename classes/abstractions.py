# abc modülünden ABC sınıfı ve abstractmethod dekoratörü yüklenir
from abc import ABC, abstractmethod

# Widget adında soyut bir sınıf (abstract class) oluşturalım.
class Widget(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def press(self):
        pass


# Button sınıfı Widget sınıfından türetilmiş olsun ve soyut metotları özelleştirsin.
class Button(Widget):
    def draw(self):
        print("Drawing a button.")


button1 = Button()
# TypeError: Can't instantiate abstract class Button without an implementation for abstract method 'press'


class Button(Widget):
    def draw(self):
        print("Drawing a button.")

    def press(self):
        print("Pressing a button.")


button2 = Button()
button2.draw()
button2.press()

issubclass(Button, ABC)


################################################################

class BasicMusicInstrument(ABC):
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand

    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def play(self):
        pass

    def __repr__(self):
        return f"{self.model}, {self.brand}"


class Guitar(BasicMusicInstrument):
    def sound(self):
        print("The Evenings of Mediternean")

    def play(self):
        print("Playing a guitar")


class Violin(BasicMusicInstrument):
    def sound(self):
        print("I am a violin")


guitar1 = Guitar("CD-100CE", "Fender")
guitar1.sound()
guitar1.play()

violin1 = Violin("Epiphone", "Gibson")
# TypeError: Can't instantiate abstract class Violin without an implementation for abstract method 'play'

