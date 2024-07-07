# String Lenght

my_str = "Hello World"
print("Stringin uzunluğu:", len(my_str))

print(my_str.__len__()) #special method

########################## String Concatenation (Birleşitrme) ###################################
first_str = "Hello"
second_str = "world!"

#String addition
sentence = first_str + " " + second_str
print(sentence)

# % operator

sentence = "%s, %s"% (first_str, second_str)
print(sentence)

# .Format() method
sentence = "{}, {}".format(first_str, second_str)
print(sentence)

a = "BilgeAdam"
b = "kursu"
c = "python"

sentence = " {0} {2} {1}".format(a, b, c)
print(sentence)

# f-string
sentence = f"{first_str}, {second_str}"
print(sentence)

#String Multiplication

letter = "7"
print(letter * 3)
print(int(letter * 3) + 3)

########################### STRİNG İNDEXİNG AND SLİCİNG #########################################

# String indexing
word = "BilgeAdam"
       #012345678
       #-9-8-7-6-5-4-3-2-1 negat
print(len(word))
print(word[0]) #ilk karakter
print(word[-9]) # ilk karakter
print(word[5]) # A
print(word[9]) # IndexError: string index out of range
print(word[-10]) # IndexError: string index out of range

print(word[-len(word)])

# String Slicing

word = "BilgeAdam"
print(word[0:5])  # start:stop; start indeksi dahil (included) stop indeksi hariç (excluded)
print(word[5:8])  # Ada
print(word[5:])
print(word[5:100])  # hata vermez
print(word[-3: -1])
print(word[-1:-5])
print(word[5:-1])

print(word[2:7:2]) # start:stop:step başlangıç:bitiş:adım

print(word[-1:-5:-1]) # madA
print(word[-1:4:-1]) # madA

print(word[2::3]) # lAm
print(word[:6:2]) #ble

# in, not in operators

word = "BilgeAdam"

print("B" in word)
print("b" in word)
print("Ada" ,n word)

print("z" not in word)

#Escape characters

txt = "Hello\bworld!"


