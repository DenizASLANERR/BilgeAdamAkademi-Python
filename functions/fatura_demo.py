# Alıştırma
# Müşteriler farklı türde ve sayıda ürün satın alabilirler. Her ürünün adı, fiyatı ve miktarı
# olacaktır. Ayrıca, faturaya özel notlar veya kampanya kodları gibi ekstra bilgiler de eklenebilir.
urun1= {"ad": "Laptop", "fiyat": 1000, "miktar":1}
urun2= {"ad": "Telefon", "fiyat": 500, "miktar":2}
urun3= {"ad": "Klavye", "fiyat": 100, "miktar":3}
urun4= {"ad": "Fare", "fiyat": 50, "miktar":2}


def fatura_olustur(*urunler, **ekstra):
    toplam = 0
    for urun in urunler:   # arbitrary arguments (*args)
        urun_tutar = urun["miktar"] * urun["fiyat"]
        toplam += urun_tutar
        print(f"{urun['ad']}\t{urun['miktar']} Adet\t${urun_tutar}")
    print(f"Toplam fatura tutarı: ${toplam}")
    for anahtar, deger in ekstra.items():
        print(f"{anahtar}\t {deger}")
        if anahtar == "kampanya" and deger == "YAZ2024":
            indirim = toplam * 0.1
            print(f"Yaz 2024 kampanyası ile ${indirim} uygulandı")
            toplam -= indirim
        elif anahtar == "kampanya" and deger == "MOTHERSDAY":
            indirim = toplam * 0.5
            print(f"MOTHERSDAY kampanyası ile ${indirim} uygulandı")
            toplam -= indirim
        if anahtar == "kargo" and deger == "Express":
            print(f"Express kargo uygulandı. Tutar $25 eklendi")
            toplam += 25
    print(f"Toplam fatura tutarı: ${toplam}")




fatura_olustur(urun1, urun2, urun3, urun4)
fatura_olustur(urun1, urun2, urun3, urun4, kargo="Express", kampanya="YAZ2024")
fatura_olustur(urun1, urun2, urun3, urun4, kargo="Express", kampanya="MOTHERSDAY")
