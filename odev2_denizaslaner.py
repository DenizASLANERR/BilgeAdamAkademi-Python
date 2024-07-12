"""
Alıştırma 1: E-posta Adresi Format Kontrolü
Açıklama: Kullanıcıdan bir e-posta adresi alın ve bu adresin geçerli bir format olup olmadığını kontrol edin.
Geçerli bir e-posta adresi için aşağıdaki kuralları uygulayın:
En az bir "@" işareti içermelidir.
"@" işaretinden önce ve sonra en az bir karakter olmalıdır.
Son kısım en az iki karakterden oluşan bir alan adı (örneğin ".com", ".net", ".org") içermelidir.
Örnek Girdi: kullanici@example.com
Örnek Çıktı: True
"""


e_post = input("E-posta adresinizi giriniz:")
post_check = e_post.split("@")

if post_check[0] == "":
    print("Bu formatta giriş yapamazsınız")
elif post_check[1] == "":
    print("Yanlış kullanım")
else:
    if ("@" in e_post and (".com" in e_post or ".net" in e_post or ".org" in e_post)):
        print("True")
        print("Başarıyla giriş yapıldı...!")
    else:
        print("Lütfen doğru formatta bir e-posta adresi giriniz")


"""
Alıştırma 2: String İçindeki Harf Sayısını Bulma
Açıklama: Kullanıcıdan bir cümle ve bir harf alın. Girilen cümle içinde, 
kullanıcının girdiği harfin kaç kez geçtiğini bulun ve ekrana yazdırın.
Örnek Cümle: "Bu bir deneme cümlesidir."
Örnek Harf: "e"
Örnek Çıktı: "e" harfi 4 kez geçmektedir.
"""

sentence = input("Cümlenizi giriniz:")
char = input("Saydırmak istediğiniz harfi giriniz:")
total_char = sentence.count(char)
print(f"Girdiğiniz cümlede {total_char} tane {char} harfi var")

"""
Alıştırma 3: Formula 1 Sıralama Simülasyonu
Açıklama: Aşağıda verilen bilgilere göre, hangi pilotun yarışı kazandığını belirleyin ve sonucu yazdırın.
Verilen Bilgiler: Pilotların isimleri ve süreleri bir liste içinde tuple olarak veriliyor.
yariscilar = [("Lewis Hamilton", 312), ("Max Verstappen", 315)]
Örnek Çıktı: Lewis Hamilton yarışı kazandı.
"""

drivers = [("Lewis Hamilton", 312), ("Max Verstappen", 315)]
winner = min(drivers)
print(f"{winner[0]} yarışı kazandı...!")

"""
Alıştırma 4: NBA Skor Takibi
Açıklama: Bir NBA maçında, iki takımın attığı basket sayılarını içeren bir liste veriliyor. Kullanıcıdan 
iki takımın adını ve her çeyrek için attıkları sayıları içeren bir liste alın ve hangi takımın kazandığını ekrana yazdırın.
Verilen Bilgiler: [("Lakers", [30, 25, 20, 25]), ("Celtics", [25, 30, 25, 20])]
Örnek Çıktı: Lakers 100 - 100 Celtics. Maç berabere bitti.
"""

first_team_name = input("İlk takımın adını giriniz:")
first_list = []
first_scores_list =[]
first_list.append(first_team_name)
counter1 = 0
while True:
    quit = input("hesaplama işlemine geçmek için 'q' harfini girin\nTakım sayıları için 'c' harfini giriniz!")
    if quit == "q":
        break
    else:
        first_scores = int(input("İlk takımın sayılarını giriniz:"))
        first_scores_list.append(first_scores)
        counter1 += 1
first_list.append(first_scores_list)
print(f" ilk takım bilgileri:{first_list}")

second_team_name = input("ikinci takımın adını giriniz:")
second_list = []
second_scores_list =[]
second_list.append(second_team_name)
counter2 = 0
while True:
    quit = input("hesaplama işlemine geçmek için 'q' harfini girin\nTakım sayıları için 'c' harfini giriniz!")
    if quit == "q":
        break
    else:
        second_scores = int(input("İkinci takımın sayılarını giriniz:"))
        second_scores_list.append(second_scores)
        counter2 += 1

second_list.append(second_scores_list)
print(f" İkinci takım bilgileri:{second_list}")

all_match = first_list + second_list
print(all_match)
total1 =sum(first_scores_list)
print(f"{first_team_name} = {total1} puan")
total2 = sum(second_scores_list)
print(f"{second_team_name} = {total2} puan")

if total1 > total2:
    print(f"Maçı {first_team_name} kazandı")
elif total1 < total2:
    print(f"Maçı {second_team_name} kazandı")
else:
    print("maç berabere bitti")












