# data types

# Numbers -> Integers,  Float, complex, longs
# Strings -> characters or text
# Booleans -> True or False

# Operators

# arithmetic operators:

# +, -, /, *, %

# Comparison operators

# >, <, ==, !=, >=, <=

# Numeric Types

a = 24
b = 16

print(a + b) # 40
print(a - b) # 8
print(a / b) # 1.5
print(a < b) # False

FloatNum = 1.356
IntNum = 4

print(type(FloatNum + IntNum))

# python round up floats
one_third = 1/3
print(one_third * 3)

# strings

# either "" or ''

escape_example = 'I said \'Wow!\''
print(escape_example)

# String slicing

hi = "Hello World!"
# strings are indexed from 0 as a 1st character

print(hi[1]) # e

print(hi[0:5]) # hello - fist index included, second index excluded
print(hi[:5]) # hello
print(hi[-5:]) # orld!

# String methods

# len() - how long the string is
print(len(hi))
# .strip() - removes whitespace
white_space = "      lot's of whitespaces                  "
print(white_space)
print(white_space.strip())

# .lower() - convert string to lowercase
example_text = "HeRe is some text"
print(example_text.lower())

# .upper() - converts string to uppercase
print(example_text.upper())

# .capitalize() - First letter capital
print(example_text.capitalize())

# .count() - count how many times specific character appears
print(example_text.count("e"))

# .replace() - replaces chosen character with what we choose
print(example_text.replace("some", "P"))

# Concatenation and Casting

x = 2
y = 5.4
z = "This is a string"
zz = "This is also a string"
#concatenation
print(z + " " + zz)
#casting
print(str(x) + " " + str(y)+ " " + z + " " + zz)

# string to numeric casting
int_string = '6'

print(int(int_string))
print(type(int(int_string)))

# F-strings
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
