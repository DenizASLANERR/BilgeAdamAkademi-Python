"""
Alıştırma: Büyük Daire Mesafesi Hesaplayıcı

Bu alıştırmada, dünya üzerindeki iki şehir arasındaki büyük daire mesafesini hesaplayan
bir Python programı yazacaksınız. Kullanıcıdan iki şehrin enlem ve boylam değerlerini (ondalık sayı olarak)
alacak ve bu değerleri kullanarak büyük daire mesafesini hesaplayacaksınız. Büyük daire mesafesi, iki nokta
arasındaki en kısa mesafedir ve Haversine formülü kullanılarak hesaplanır.

İstenilenler:
Kullanıcıdan iki şehrin enlem ve boylam değerlerini al.
Haversine formülünü kullanarak büyük daire mesafesini hesapla.
Hesaplanan mesafeyi ekrana yazdır.
Çıktı:
Birinci şehrin enlem değerini giriniz: 41.0082
Birinci şehrin boylam değerini giriniz: 28.9784
İkinci şehrin enlem değerini giriniz: 40.7128
İkinci şehrin boylam değerini giriniz: -74.0060
İki şehir arasındaki büyük daire mesafesi: 8031.77 km
"""
import math
from math import radians, cos, sin, asin, sqrt
city1_lat = float(input("1. şehrin enlem değerlerini giriniz: "))
city1_lon = float(input("1. şehrin boylam değerlerini giriniz:"))
city2_lat = float(input("2. şehrin enlem değerlerini giriniz:"))
city2_lon = float(input("2. şehrin boylam değerlerini giriniz:"))

city1_lat, city1_lon, city2_lat, city2_lon = map(radians, [city1_lat, city1_lon, city2_lat, city2_lon])
dlat = city2_lat - city1_lat
dlon = city2_lon - city1_lon
a = math.sin(dlat / 2) ** 2 + math.cos(city1_lat) * math.cos(city2_lat) * math.sin(dlon / 2) ** 2
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
r = 6371
d = c * r

print("iki şehir arasındaki büyük daire mesafesi:", d)


