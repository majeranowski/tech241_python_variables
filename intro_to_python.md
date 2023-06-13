# Intro to Python

a way to store data within a program -> it becomes a reference to that data
 variable can change. it is mutable

 how to set a variable in python

 ```a = 4``` -> variable_name = variable_data
 
### Dynamically typed language - Python
``` python
a = 1 #int
b = 2 #int
c = 3.5 #float
hi = "My name is Krzychu" #string

print(a + b)
```
### Strong typed language in Java
```Java 
 int a = 1;
 float c = 3.5;
```

### variables can be overwritten
```python
d = 5
print(d)
d = 7
print(d)
```

### user input

```python
name = input("What is your name? ")
age = input("What is your age? ")
dob = input("What is your date of birth? ")
address = input("What is your address? ")
print(f"The user's name is {name}, age is {age} years with date of birth {dob} and lives in {address}.")
#print("Hi, " + name + " You are " + age + " years old, born on " + dob + " and you live in " + address)

```

### data types

* Numbers -> Integers,  Float, complex, longs
* Strings -> characters or text
* Booleans -> True or False

### Operators

##### arithmetic operators:
* +, -, /, *, %

##### Comparison operators:
* <, >, ==, !=, >=, <=

### Numeric data types:

```python
a = 24
b = 16

print(a + b) # 40
print(a - b) # 8
print(a / b) # 1.5
print(a < b) # False

FloatNum = 1.356
IntNum = 4

print(type(FloatNum + IntNum))
```
python round up floats:
```python
one_third = 1/3 #equals 0.333333
print(one_third * 3) # equals 1.0
```
### String data types:
We can use either  " " or ' ' to assign a string to a variable

Example of using escape character:

```python
escape_example = 'I said \'Wow!\''
print(escape_example)
```
##### String slicing


strings are indexed from 0 as a 1st character
```python
hi = "Hello World!"
print(hi[1]) # e
print(hi[0:5]) # hello - fist index included, second index excluded
print(hi[:5]) # hello
print(hi[-5:]) # orld!
```
##### String methods

* len() - how long the string is

`print(len(hi))`
* .strip() - removes whitespace
```python
white_space = "      lot's of whitespaces                  "
print(white_space)
print(white_space.strip())
```

* .lower() - convert string to lowercase
```python
example_text = "HeRe is some text"
print(example_text.lower())
```

* .upper() - converts string to uppercase

`print(example_text.upper())`

* .capitalize() - First letter capital

`print(example_text.capitalize())`

* .count() - count how many times specific character appears

`print(example_text.count("e"))`

* .replace() - replaces chosen character with what we choose

`print(example_text.replace("some", "P"))`

##### Concatenation and Casting
```python
x = 2
y = 5.4
z = "This is a string"
zz = "This is also a string"
#concatenation
print(z + " " + zz)
#casting
print(str(x) + " " + str(y)+ " " + z + " " + zz)
```

##### string to numeric casting
```python
int_string = '6'

print(int(int_string))
print(type(int(int_string)))
```
##### F-strings
```python
name = "Lassie"
years = 7
height = 60.2

print(f"My dog name is {name.upper()}, he is {years * 7} in dog years old and {height}cm tall")

pi = 3.14159265

print(f"Pi to 3 decimal places: {pi:.3f}")

# percentages

score = 16
max_score = 26

print(f"You scored {(score/max_score):.0%}")
```
### Booleans
```python
a = True
b = False

print(a == b) #False
print(a != b) # True
print(a >= True) # True
```
### Using keywords
```python
print (True and False) # False
print (True or False) # True
```

### Boolean methods
```python
hi = "hello world!"
print(hi.isalpha()) #False (true only if it is just alphabetical)
print(hi.islower()) #True
print(hi.endswith("!")) #True (with what character it ends
print(hi.startswith("H")) #False because it starts with 'h'
```


##### The value of 0
```python
x = 0
y = 10
print(bool(x)) # 0 is always false, other numbers are True
print(bool(y))
```


##### value of None

Not 0, not nothing -----> it is a PLACEHOLDER
```python
print(bool(None)) # False
print(None == False) #False
print(None == True) #False
#None is None, independent from True and False
```


##### best practice for checking if something is None
```python
p = None
print(p is None)
```

