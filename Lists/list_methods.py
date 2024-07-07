####### range() ########

# range(stop)
myrange = range(10)
print(myrange, type(myrange))

for i in range(10):
    print(i)

mylist = list(myrange)
print(mylist)

# range(start, stop)
myrange = range(5, 10)
print(list(myrange))

# range(start, stop, step)
myrange = range(5, 10, 2)
print(list(myrange))

myrange = range(10, 5, -1)
print(list(myrange))

for i in range(100):
    print(i ** 2)


# append(): sonuna eleman ekler
mylist = list(range(5))
print(mylist)

mylist.append(5)

a = mylist.append(6)
print(a)
print(mylist)

# extend(): liste uzatma
new_list = [6, 7, 8]

mylist.extend(new_list)
print(mylist)

mylist.extend(range(8, 10))
print(mylist)

mylist.extend("apple")
print(mylist)

# insert(): belirli bir indekse eleman ekler

mylist.insert(3,"iki")
print(mylist)

# remove(): Eleman silmek
mylist.remove("iki")
print(mylist)

# pop(): indeks numarasından silmek
mylist.pop(1)
print(mylist)

popped_item = mylist.pop()
print(f"çıkarılan değer: {popped_item}\nListenin yeni hali: {mylist}")

# index(): elemanın indeksini bulma

mylist.index(3)
mylist.index(8)

#count(): elemanın tekrar etme sayısını bulmak

mylist.count(8)

# sort(): Liste sıralama

mylist = [5, 5, 2, 12, 32, 3, 12, 45, 85, 976, 45, 12]

#Küçükten büyüğe sırala ve yeni bir nesne oluştur

mylist_sorted = sorted(mylist)
print(mylist)
print(mylist_sorted)
# büyükten küçüğe
sorted(mylist, reverse=True)
print(mylist)

#küçükten büyüğe sırala ve bu değişim kalıcı olsun
mylist.sort()
print(mylist)

#büyükten küçüğe

mylist.sort(reverse=True)
print(mylist)

str_list = ["a", "b", "c", "ayt", "z", "eft", "eyt", "ayt", "oks"]

str_list.sort()
print(str_list)

#reverse(): lsiteyi terse çevirir
mylist = [5, 5, 2, 12, 32, 3, 12, 45, 85, 976, 45, 12]

mylist.reverse()
print(mylist)

#copy(): liste kopyalama

a = [1, 2]
print(a, id(a))

b = a
print(b, id(b))

b[0] = 6
print("b:", b)
print("a:", a)

c = [a.copy()]
print(c, id(c))
c[0] = 9
print(a, id(a))
print(c, id(c))





