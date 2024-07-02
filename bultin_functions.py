##################### GÖMÜLÜ FONKSİYONLAR ######################
# https://docs.python.org/3/library/functions.html

# input() fonksiyonu
numerator = input("Pay kısmını giriniz=  ")
denominator = input("Payda kısmını giriniz= ")

result = int(int(numerator) / int(denominator))
print("Sonuç =", result)

# ord() fonksiyonu
character = 'A'
unicode_value = ord(character)
print(character, unicode_value)

character = 'a'
unicode_value = ord(character)
print(character, unicode_value)

prompt = "Unicode değerini istediğiniz karakteri giriniz: "
character = input(prompt)
unicode_value = ord(character)
print(character, unicode_value)

# chr() fonksiyonu
unicode_value = 97
character = chr(unicode_value)
print(f"Unicode değeri: {unicode_value} - Karakter: {character}")   # f-string

prompt = "Karakterini çıktı almak istediğiniz Unicode değerini giriniz: "
unicode_value = int(input(prompt))
character = chr(unicode_value)
print(f"Unicode değeri: {unicode_value} - Karakter: {character}")   # f-string