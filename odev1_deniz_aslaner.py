"""
Alıştırma 1. Sıcaklık Dönüştürücü (Celsius'tan Fahrenheit'a)
Kullanıcıdan Celsius sıcaklık değerini (ondalık sayı olabilir)
girmesini isteyen, girilen değeri Fahrenheit dereceye dönüştüren
ve sonucu yazdıran kısa bir Python programı yazın.
"""
while True:
    islem = int(input("°C'dan °F işlemi için 1'e \n°F'dan °C'a çevirmek için 2'ye basınız \nProgramdan çıkmak için 3'e basınız:"))
    if (islem == 3):
        print("Programdan çıkılıyor...")
        break
    elif (islem == 1):
        celsius = float(input("Celsius °C sıcaklık değerini giriniz:"))
        fahrenheit = (celsius * 1.8) + 32
        print("Girdiğiniz {}°C değerine karşılık gelen değer {}°F'dır.".format(celsius, fahrenheit))
    elif (islem == 2):
        fahrenheit = float(input("Fahrenheit °F sıcaklık değerini giriniz:"))
        celsius = (fahrenheit - 32) * 1.8
        print("Girdiğiniz {}°F değerine karşılık gelen değer {}°C'dur.".format(fahrenheit, celsius))
    else:
        print("Geçersiz bir işlem girdiniz!!! Lütfen geçerli bir işlem seçiniz :")

""" 
Alıştırma 2. Mesafe Dönüştürücü (Kilometreden Mile)
Kullanıcıdan kilometre cinsinden bir mesafe (ondalık bir
sayı olabilir) girmesini isteyen, girilen mesafeyi mile
çeviren ve sonucu yazdıran kısa bir Python programı yazın.
"""
while True:
    secenek = input("Programdan çıkmak için 'q' harfine basınız:\nKM'den mile çevirmek için 1'e basınız:\nMilden KM'ye çevirmek için 2'ye basınız:")
    if (secenek == "q"):
        print("Program Kapatılıyor...")
        break
    elif (secenek == "1"):
        km = float(input("Kilometre cinsinden bir mesafe giriniz:"))
        mile = km / 1.609344
        print("mil:{}".format(mile))
    elif (secenek == "2"):
        mile = float(input("Mil cinsinden bir mesafe giriniz:"))
        km = mile * 1.609344
        print("KM:{}".format(km))
    else:
        print("Lütfen tanımlı bir işlem seçiniz:")
"""
Alıştırma 3. Üçgen Alan Hesaplayıcı Kullanıcıdan bir üçgenin 
taban ve yüksekliğini (ondalık sayı olabilir) alacak bir program yazın.
Program, bu değerleri kullanarak üçgenin alanını hesaplamalı ve sonucu 
yazdırmalıdır. (Üçgenin alanı hesaplama formülü: (taban x yükseklik) / 2)
"""
print("#################### Üçgen Alan Hesabı Programı ####################")

while True:
    islem = input("Programdan çıkmak için 'q' harfine basınız\nÜçgenin alanını hesaplamak için 1 tuşuna basınız:\nÜçgenin yüksekliğini hesaplamak için 2 tuşuna basınız:\nÜçgenin taban ölçülerini hesaplamak için 3 tuşuna basınız:")
    if (islem == "q"):
        print("Programdan çıkılıyor...")
        break
    elif (islem == "1"):
        base_of_triangel = float(input("Üçgenin tabanını giriniz:"))
        height_of_triangel = float(input("Üçgenin yüksekliğini giriniz:"))
        area_of_triangel = (base_of_triangel * height_of_triangel) / 2
        print("Üçgenin alanı:{}".format(area_of_triangel))
    elif (islem == "2"):
        area_of_triangel = float(input("Üçgenin alanını giriniz:"))
        base_of_triangel = float(input("Üçgenin tabanını giriniz:"))
        height_of_triangel = (area_of_triangel * 2) / base_of_triangel
        print("Üçgenin yüksekliği:{}".format(height_of_triangel))
    elif (islem =="3"):
        area_of_triangel = float(input("Üçgenin alanını giriniz:"))
        height_of_triangel = float(input("Üçgenin yüksekliğini giriniz:"))
        base_of_triangel = (area_of_triangel * 2) / height_of_triangel
        print("Üçgenin tabanı:{}".format(base_of_triangel))
    else:print("\nGeçersiz işlem girdiniz!!!\nLütfen geçerli işlemlerden birini seçerek tekrar deneyiniz!\n")

"""
Alıştırma 4. Ortalama Sıcaklık Hesaplayıcı Kullanıcıdan bir şehir ve bu şehirde ölçülen bir günün en yüksek
ve en düşük sıcaklıklarını (ondalık sayı olarak) alacak bir Python programı yazın. Program bu bilgileri 
kullanarak o gün için ortalama sıcaklığı hesaplamalı ve şu formatta ekrana yazdırmalıdır:
"""
print("###################### Şehir Ortalama Sıcaklık Hesaplayıcı ######################")
city = input("Şehri giriniz:")
hottest = float(input("Ölçülen en yüksek sıcaklığı giriniz:"))
coldest = float(input("Ölçülen en düşük sıcaklığı giriniz:"))
avg = (hottest + coldest) / 2
print("Şehir:{}\nEn Yüksek Sıcaklık:{}\nEn Düşük Sıcaklık:{}\nOrtalama Sıcaklık:{}\n".format(city,hottest,coldest,avg))




