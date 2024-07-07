#title(): Her kelimenin ilk harfini büyük yapar

expression = "python course"
print(type(expression))
print(expression.title())
print(expression)

# capitalize(): Tüm ifadenin ilk harfini büyük yapar
print(expression.upper())

# upper()
print(expression.upper())

# lower()
print(expression.lower())

print(expression.title().lower().upper().capitalize()) # zincirleme

# startswith(): belirlenen bir substring ile başlayıp başlamadığını kontrol eder
print(expression.startswith("p")) # True
print(expression.startswith("P")) # False
print(expression.startswith("pyt")) # True
print(expression.startswith("python ")) # True

print(expression.title().startswith("P")) # True

print(expression[::-1].startswith("es")) #True

# endswith():
print(expression.endswith("se"))
print(expression.endswith("course"))
print(expression.endswith(" "))
print(expression.endswith("")) #True
#print(expression.endswith(None)) #TypeError: endswith first arg must be str or a tuple of str, not NoneType

#find(): ilk bulduğu substring başlangıç indeksini döndürür, bulamazsa -1
print(expression.find("p"))
print(expression.find("P"))
print(expression.find("thon")) #2
print(expression.find("ton")) #-1

print(expression.index("thon")) #2
print(expression.index("ton")) #ValueError: substring not found

# isdigit()

print(expression.isdigit())
numbers = "0123456789"
print(numbers.isdigit())
mixed_str = "123a123"
print(mixed_str.isdigit())

#istitle()
print(expression.istitle())
print(expression.title().istitle())

#isupper(), islower()
print(expression.isupper())
print(expression.islower())
print(expression.title().islower())

#isalpha()
print(expression.isalpha())
print("pythoncourse".isalpha())

#isalnum()
print(expression.isalnum()) #false
print("pythoncourse2".isalnum())

#isascii()
print(expression.isascii())
print("Türkiye".isascii()) #false
print("123asd.?".isascii()) #true

#split():belirtilen karakter (seperator) ile stringini böler ve bu substringleri listeye atar
print(expression.split(" ")) #boşluk işareti ile stringi böldü ve her bölümü bir listeye ekledi
print(expression.split(" ")[0]) #list indexing
print("1234x45x34x987".split("x"))
print("1234x 45x34x987".split("x "))

#strip():her iki tarafta fa belirtilen karakteri siler (kırpar)
name = "  BilgeAdam  "
trimmed_name = name.strip(" ")
print(trimmed_name)

#rstrip(): sağdan kırpma yapar
right_trimmed_name = name.rstrip(" ")
print(right_trimmed_name)

#lstrip(): soldam kırpar
left_trimmed_name = name.lstrip()
print(left_trimmed_name)

#replace()
print(expression.replace("python", "java").title())

#count()
e_mail = "mjordan@gmail.com, kbryant@gmail.com"
print(e_mail.count("@gmail"))

#swapcase()
print(expression.title().swapcase())

#join()
mylist = ["Ali", "Veli", "Mehmet"]
print("&".join(mylist))



















