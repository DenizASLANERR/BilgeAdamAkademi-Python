#conditional statements (koşullu ifadeler)

#if statement
if True:
    print("This expression is True") #bir girinti (indentation)
if False:
    print("This expression is false") #bu koda erişilemez

age = int(input("What is your age?:"))

if age >= 18:
    print("you're an adult")
else:
    print("you're not an adult")
#----------------------------------------
if age >= 18:
    print("you're an adult")
elif 0 < age < 18:
    print("you're not an adult")
else:
    print("Invalid age")

mylist = []

if mylist:
    print("A")
else:
    print("B")



if "":
    print("A")
else: