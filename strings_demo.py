# Alıştırma 1. 'website' değişkenindeki 'spacex' ifadesini yalnız bırakacak kodu yazınız.
website = "http://www.spacex.com/"
print(website.strip("ht/p:w.com"))
print(website.split(".")[1])

# Alıştırma 2. 'python değişkeninde bulunan "python" ifadesi yerine "java" ifadesi koyunuz ve
# başlık formatına çeviriniz.
python = "python application course"
print(python.replace("python", "java").title())

# Alıştırma 3. 'phrase' değişkenindeki isimleri listeye atayacak şekilde işleyiniz.
phrase = "Ali, Ahmet, Veli, Serhat"
print(phrase.split(", "))