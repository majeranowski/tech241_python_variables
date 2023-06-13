# variables in python

# a way to store data within a program -> it becomes a reference to that data
# variable can change. it is mutable

# how to set a variable in python

# a = 4 -> variable_name = variable_data
# Dynamically typed language - Python

a = 1 #int
b = 2 #int
c = 3.5 #float
hi = "My name is Krzychu" #string

print(a + b)

 #Strong typed languagein Java
 # int a = 1;
 # float c = 3.5;

# type() method

print(type(hi))

#variables can be overwritten

d = 5
print(d)
d = 7
print(d)


# user input

name = input("What is your name? ")
age = int(input("What is your age? "))
dob = input("What is your date of birth? ")
address = input("What is your address? ")
hobby = input("What is your hobby? ")
print(f"The user's name is {name}, age is {age} years with date of birth {dob}, lives in {address} and the hobby is {hobby}.")
#print("Hi, " + name + " You are " + age + " years old, born on " + dob + " and you live in " + address)


