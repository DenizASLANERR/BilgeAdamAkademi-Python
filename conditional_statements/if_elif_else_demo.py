#kullanıcıdan sınav notunu (100 üzerinden) isteyen
#Derse ait harf çıktı veren bir if-elif-else kod bloğı yazın
# >= 90: A
# >= 80: B
# >= 70: C
# >= 60: D
# < 60: F
try:
    score = float(input("Ders notunuzu(0-100 arasında) giriniz:"))

    if 0 <= score <= 100:
        if score >= 90:
            print("Ders notunuz:A")
        elif score >= 80:
            print("Ders notunuz:B")
        elif score >= 70:
            print("Ders notunuz:C")
        elif score >=60:
            print("Ders notunuz:D")
        else:
            print("Ders notunuz:F")
    else:
        print("(0-100) arası bir değer girmediniz!")
    print("program sonlandı")

except ValueError:
    print("Bir sayı girmediniz")
