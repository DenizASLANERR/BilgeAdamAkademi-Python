################### TİP DÖNÜŞÜMLERİ ##########################

#### int() #####

# float to int
x = 5.5   # <class 'float'>
print(type(x))

y = int(x)
print(y, type(y))    # 5 <class 'int'>

# bool to int
x = False
y = int(x)
print(y, type(y))    # 0 <class 'int'>

# str to int
x = "5"
y = int(x)
print(y, type(y))     # 5 <class 'int'>

x = "5O"
y = int(x)   # ValueError: invalid literal for int() with base 10: '5O'
print(y, type(y))

# None to int
x = None
y = int(x)     # TypeError
print(y, type(y))

########### float() ###########
# int to float
x = 5
y = float(x)
print(y, type(y))   # 5.0 <class 'float'>

# str to float
x = "5.2"
y = float(x)
print(y, type(y))    # 5.2 <class 'float'>

# bool to float
x = True
y = float(x)
print(y, type(y))     # 1.0 <class 'float'>

################ bool() #######################
# int to bool
x = 1
y = bool(x)
print(y, type(y))    # True <class 'bool'>

x = 0
y = bool(x)
print(y, type(y))     # False <class 'bool'>

x = -5
y = bool(x)
print(y, type(y))     # True <class 'bool'>

# float to bool
x = 0.0
y = bool(x)
print(y, type(y))    # False <class 'bool'>

x = -0.0005
y = bool(x)
print(y, type(y))    # True <class 'bool'>


# str to bool
x = ""
y = bool(x)
print(y, type(y))    # False <class 'bool'>

x = " "
y = bool(x)
print(y, type(y))    #True <class 'bool'>

# NoneType to bool
x = None
y = bool(x)
print(y, type(y))     # False <class 'bool'>

#################### str() ##################
# int to str
x = 5
y = str(x)
print(y, type(y))    # 5 <class 'str'>

# float to str
x = 5.0
y = str(x)
print(y, type(y))   # 5.0 <class 'str'>

# None to str
x = None
y = str(x)
print(y, type(y))   # None <class 'str'>

# bool to str
x = True
y = str(x)
print(y, type(y))    # True <class 'str'>