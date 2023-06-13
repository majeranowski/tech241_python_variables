# Booleans

a = True
b = False

print(a == b) #False
print(a != b) # True
print(a >= True) # True

# Using keywords

print (True and False) # False
print (True or False) # True

#Booleans with data types

hi = "hello world!"

# Boolean methods

print(hi.isalpha()) #False (true only if it is just alphabetical)
print(hi.islower()) #True
print(hi.endswith("!")) #True (with what character it ends
print(hi.startswith("H")) #False because it starts with 'h'

#The value of 0

x = 0
y = 10
print(bool(x)) # 0 is always false, other numbers are True
print(bool(y))

#value of None

#Not 0, not nothing -----> it is a PLACEHOLDER

print(bool(None)) # False
print(None == False) #False
print(None == True) #False
#None is None, independent from True and False

# best practice for checking if something is None
p = None
print(p is None)
