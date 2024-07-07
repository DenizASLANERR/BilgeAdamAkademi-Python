import math
import time
# kullanıcıdan daire yuarıçapı (r) alan ve dairenin alanı ve çevresini hesapla.

r = float(input("daire yarı çapını giriniz:"))
print("Dairenin alanı hesaplanıyor...")
time.sleep(2)
A = math.pi * r ** 2
print("Direnin alanı:",round(A, 2), "cm^2")
print("Dairenin çevresi hesaplanıyor...")
time.sleep(2)
cevre = 2 * math.pi * r
print("Çevresi:", round(cevre, 2), "cm")
