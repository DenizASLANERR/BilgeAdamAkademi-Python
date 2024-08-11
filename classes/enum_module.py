from enum import Enum, auto


# Enum sınıfından türetilmiş bir 'Weekday' sınıfı tanımlayın
class Weekday(Enum):
    MONDAY = 1  # Constant (sabit) adı ve değeri
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


issubclass(Weekday, Enum)


print(type(Enum))
print(type(Weekday))

print(list(Weekday))

print(Weekday.MONDAY.name)
print(Weekday.MONDAY.value)

# Enum üyeleri değiştirilemezler.
Weekday.MONDAY = 8   # AttributeError: cannot reassign member 'MONDAY'


class Season(Enum):
    WINTER, SPRING, SUMMER, FALL = range(1,5)


print(Season.SPRING.name)
print(Season.SPRING.value)


class Weekday(Enum):
    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()
    SATURDAY = auto()
    SUNDAY = auto()


print(Weekday.SATURDAY.value)




