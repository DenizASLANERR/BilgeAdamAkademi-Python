#Tuple (demet) oluşturmak
empyt_tuple = () #boş tuple
one_element_tuple = (1,) #bir elemanlı tuple
mytuple = (1, 2, 3, 3, 4, 2, 2, 6) #ordered, unchangeable (immutable)

print(type(mytuple)) #<class 'tuple'>
print(len(mytuple))

#tuple'ın elemanlarına erişme
print(mytuple[2])


#slicing ile birden çok elemanına erişme (subtuple)
print(mytuple[2:5])

#bir elemanın tuple'ın içerisinde olup olmadığını öğrenme
print(3 in mytuple) #True
print(10 not in mytuple) #True

#Immutable
mytuple[1] = 5 #TypeError: 'tuple' object does not support item assignment



