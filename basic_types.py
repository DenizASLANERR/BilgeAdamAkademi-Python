# Python'da Temel Veri Tipleri
# str (string) metin  --> "car", 'tire'
# int (integer) tam sayı   --> 5, 6, 7, 1_000_000, -5
# float (float) ondalıklı sayı  ---> 5.2, 7.89, 0.0
# bool (boolean) mantık ifadesi  ---> True, False
# complex (complex) karmaşık sayı   --> 1j
# NoneType (None)  --> None

##################### STRINGS (METINLER) #######################
mystr = "This is a string."
print(mystr)

# Metinleri farklı satırlarda yazma
mystr = ("This is a "
         "string.")
print(mystr)

# Bir değişkenin tipini incelemek
print(type(mystr))    # <class 'str'>

# Triple Quotes  (Docstrings)
mystr = """BilgeAdam
Python
Course"""

print(mystr)

mystr2 = "BilgeAdam\nPython\nCourse"
print(mystr2)

mystr3 = "BilgeAdam\tPython\tCourse"
print(mystr3)

###################### INTEGERS & FLOATS ##########################
x = 5
print(type(x))    # <class 'int'>

y = 5.0
print(type(y))    # <class 'float'>

z = 2 + 1j
print(type(z))     # <class 'complex'>

####################### BOOLEANS (MANTIKSAL) ###########################
mybool = False
print(type(mybool))    # <class 'bool'>
print(mybool)

# VE (AND) İŞLEMLERİ
salim = True
deniz = True

print(salim and deniz)   # True
print(not salim and deniz)  # False and True = False
print(salim and not deniz)  # True and False = False

yunus = True

print(salim and deniz and not yunus)    # False
print(not salim and not deniz and not yunus)   # False
print(not (not salim and not deniz and not yunus))   # True


# VEYA (OR) İŞLEMLERİ
print(salim or deniz)   # True or True = True
print(not salim or deniz)   # False or True = True
print(salim or not deniz)   # True or False = True
print(not salim or not deniz)   # False or False = False


########################### NONETYPE ###########################
mynone = None
print(mynone)
print(type(None))    # <class 'NoneType'>

print(True and None)     # None

print(True and bool(None))   # False