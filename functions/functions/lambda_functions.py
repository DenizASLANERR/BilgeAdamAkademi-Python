def square(x):
    return x ** 2

squared = lambda x: x ** 2
squared(3)


#map fonksiyonunda anonim (lambda) fonksiyon kullanmak
numbers = list(range(0, 100, 4))
print(numbers)

squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)

list(map(lambda x: x % 3 == 0, range(100)))

#filter fonk ile lambda fonksiyonu kullanmak

list(filter(list(map(lambda x: x % 3 == 0, range(100)))))
