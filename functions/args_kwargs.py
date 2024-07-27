# Arbitrary Arguments (Keyfi sayıda argümanlar), *args

def topla(*nums):
    toplam = 0
    for num in nums:
        toplam += num
    return toplam


topla(2, 3, 4, 5, 6)
topla(3)


def fonksiyonum(baslangic, bitis, *sayilar):
    print(f"baslangic argümanının aldığı değer {baslangic}")
    print(f"bitis argümanının aldığı değer {bitis}")
    print(f"sayilar keyfi argümanının aldığı değer {sayilar}")
    return sayilar


ciktim = fonksiyonum(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(ciktim)


# Arbitrary Keyword Arguments, **kwargs
# Fonksiyonun keyfi (arbitrary) sayıda keyword (anahtar kelime) argümanı almasını sağlar.
# Fonksiyonun içerisinde * args bir tuple olarak, **kwargs bir dict olarak saklanır.

def print_info(**kwargs):
    return kwargs


print_info(name="Ali", age=20, city="Ankara", salary=20000)


def print_info(**info):
    for key, value in info.items():
        print(f"Key: {key}, Value: {value}")


print_info(name="Ali", age=20, city="Ankara", salary=20000)


# *args ve **kwargs birlikte kullanımı

def mixed_func(*args, **kwargs):
    print("Positional Arguments:", args)
    print("Keyword Arguments:", kwargs)


mixed_func(1, 2, 3)
mixed_func(1, 2, 3, name="Ali", age=20)


def scrambled_func(a, b, c=5, d=7, *args, **kwargs):
    print(f"Konumsal: {a}, {b}")
    print(f"Anahtar Kelime: {c}, {d}")
    print(f"Keyfi Sayıda Konumsal: {args}")
    print(f"Keyfi Sayıda Anahtar Kelime: {kwargs}")


scrambled_func(7, 8)
scrambled_func(7, 8, 6)
scrambled_func(7, 8, 6, 9)
scrambled_func(7, 8, 6, 9, 1, 2, 3)
scrambled_func(7, 8, 6, 9, 1, 2, 3, name="Ali", age=20)

