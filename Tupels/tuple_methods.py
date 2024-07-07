mytuple = (1, 2, 3, 1, 2, 2, 6, 4)

#count(): verilen değerlerin tekrar etme sayısı
mytuple.count(2)

#index(): verilen değerin index numarasını döndürür
mytuple.index(4)
mytuple.index(2, 3)
mytuple.index(6, 1, 5) #ValueError: tuple.index(x): x not in tuple

# Error Handing
try:
    mytuple.index(6, 1, 5)
except:
    print("Girdiğiniz değer tupleiçerisinde bu aralıkta değildir!")

# tuple birleşitrme
first_tuple = (1, 3)
second_tuple = (2, 4)

third_tuple = first_tuple + second_tuple
print(third_tuple)

fourth_tuple = [first_tuple] + [second_tuple]
print(fourth_tuple)

# Tuple elemanlarını değişkenlere atama
team1 = ("Galatasaray", "Türkiye")
team, country = team1

team, country, points = team1 #ValueError: not enough values to unpack (expected 3, got 2)
























