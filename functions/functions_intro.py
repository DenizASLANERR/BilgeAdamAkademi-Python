#def keyword

def name_of_function(arg1, arg2, arg3):
    """
    This function prints out ....
    :param arg1: this is the first arg
    :param arg2: this is the second...
    :param arg3: this is the third...
    :return: 
    """#docstring(functions, classes)
    #code block
    pass
#Calling a function
name_of_function(1, "iki", True)
name_of_function(1, 2) #TypeError: name_of_function() missing 1 required positional argument: 'arg3'

# Type
print(type(name_of_function)) #<class 'function'>


# Input (girdi) almayan ve bir şey döndürmeyen(return) fonksiyon
def say_hallo():
    """
    Bu fonk 'hello' print eder
    :return:
    """
    print("Hello")

#fonksiyon çağırmak
say_hallo()
print(say_hallo()) #say_hello() --> print(None)


x = say_hallo() #ekrana 'hello' print eder
print(x) #None yazdırır, çünkü say_hello() None döndürür(return)

#help() built-in function
help(say_hallo)

#argüman alan ve bir şey print eden ve bir şey döndürmeyen (return) fonksiyon

def say_hello(name: str):
    """
    Bu fonksiyon 'Hekko,name' print eder
    :param name:
    :return:
    """
    print("Hello", name)

say_hello("bob")
say_hello(5)
say_hello(name="charlie")

say_hello() #TypeError: say_hello() missing 1 required positional argument: 'name'

#required positional argument: zorunlu konumsal argüman

# iki argüman alan ve iki farklı ifade print eden fonk

def say_hello_goodbye(name1: str, name2: str):
    print("Hello", name1)
    print("Goodbye", name2)

say_hello_goodbye("james", "Michelle")
say_hello_goodbye(name1="james", name2="Michelle")
say_hello_goodbye(name2="james", name1="Michelle") # keyword arguments
say_hello_goodbye("james", "Michelle") # positional arguments

#konumsal argüman keyword argümandan önce gelir
say_hello_goodbye("james", name2="Michelle")
#say_hello_goodbye(name2="james", "Michelle") #SyntaxError: positional argument follows keyword argument
#say_hello_goodbye(name1="james", "Michelle") #SyntaxError: positional argument follows keyword argument




#keyword arguments
def say_hello_goodbye(name1="james", name2="michelle"):
    print("Hello", name1)
    print("Goodbye", name2)

say_hello_goodbye() #default(varsayılan) değerler atanır
say_hello_goodbye(name1="nancy")
say_hello_goodbye(name2="nancy")
say_hello_goodbye(name2="nancy", name1="oscar")
say_hello_goodbye("nancy", "oscar")
say_hello_goodbye("nancy", name2="oscar")

def say_hgw(name1, name2="james", name3="michelle"):
    print("hello",name1)
    print("goodbye", name2)
    print("welcome", name3)

say_hgw() #TypeError: say_hgw() missing 1 required positional argument: 'name1'
say_hgw("brian")
say_hgw("brian", "Dennis")
say_hgw("brian", "dennis", "oscar")
say_hgw("brian", name3="oscar")

#return keyword: Bir fonksiyon çalıştırıldıktan sonra nesne(ler) döndürülmesini sağlar

def square(x):
    """
    This function gets an integer and returns the square of the number
    :param x: This needs to be an integer
    :return: Square of thr number
    """
    squared_x = x * x
    return squared_x


print(square(9)) #print(81)
print(type(square(9))) #class 'int'


def my_func(mybool: bool):
    if mybool:
        return "True"
    else:
        return 0

print(type(my_func(True))) #class str
print(type(my_func(False))) #class int


x = 8
y = square(x)
print(f"The square of {x} is {y}")
print(f"The type of {y} is {type(y)}")


#örnek:

def add_numbers(num1: float, num2: float, num3: float) -> float:
    return num1 + num2 + num3

add_numbers(4.2, 5.3, 6.4)
add_numbers("a", "b", "c") #kod hata vermez, editör uyarı verir


#tek satırda fonksiyon yazmak

def multiply_numbers(num1, num2, num3): return num1 * num2 * num3

x = multiply_numbers(4.2, 5.3, 6.4)
print(x)

#kendi oluştruduğumuz fonksiyonu map() ile kullanmak

numbers = list(range(0, 50, 3))
print(numbers)

#f(x) = 2 * x ** 2 + 3 * x + 4

def f(x):
    return 2 * x ** 2 + 3 * x + 4

for i in map(f, numbers):
    print(i, end=" ")

print(list(map(f, numbers)))

# Alıştırma 1: even_check() isimli bir kullanıcı tanımlı fonksiyon (user-defined function) oluşturun.
#              Bir int sayı alsın be bu sayının çift olup olmadığını döndürsün.


# Alıştırma 2: even_check_list() isimli bir kullanıcı tanımlı fonksiyon oluşturun.
#              Verilen bir listenin içerisinde bir çift sayı olup olmadığını kontrol etsin.
mylist1 = [1, 3, 5, 7, 8, 9]  # True
mylist2 = [1, 3, 5, 7, 9, 11]  # False
def even_check_list(mylist):
    for i in mylist:
        if i % 2 == 0:
            return True
    return False


even_check_list(mylist1)
even_check_list(mylist2)