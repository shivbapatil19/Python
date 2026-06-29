# ==========================================================
# PYTHON BASICS
# File Name : 01_Python_Basics.py
# Author    : Shivba Patil
#
# Topics Covered
# 1. Print Statement
# 2. Variables
# 3. Data Types
# 4. User Input
# 5. Type Casting
# 6. Arithmetic Operators
# 7. Practice Questions
# ==========================================================

# ==========================================================
# Question 1
# Print "Hello World"
# ==========================================================

print("Hello World")


# ==========================================================
# Question 2
# Store your name and age in variables
# ==========================================================

name = "Shivba"
age = 22

print("Name :", name)
print("Age :", age)


# ==========================================================
# Question 3
# Display different data types
# ==========================================================

integer_value = 10
float_value = 10.5
string_value = "Python"
boolean_value = True

print(type(integer_value))
print(type(float_value))
print(type(string_value))
print(type(boolean_value))


# ==========================================================
# Question 4
# Take user's name as input
# ==========================================================

name = input("Enter your name : ")

print("Welcome", name)


# ==========================================================
# Question 5
# Add two numbers
# ==========================================================

num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))

sum_result = num1 + num2

print("Sum =", sum_result)


# ==========================================================
# Question 6
# Find area of rectangle
# ==========================================================

length = float(input("Enter Length : "))
width = float(input("Enter Width : "))

area = length * width

print("Area =", area)


# ==========================================================
# Question 7
# Swap two variables
# ==========================================================

a = 10
b = 20

print("Before Swapping")
print("a =", a)
print("b =", b)

a, b = b, a

print("After Swapping")
print("a =", a)
print("b =", b)


# ==========================================================
# Question 8
# Calculate square of a number
# ==========================================================

number = int(input("Enter a Number : "))

square = number ** 2

print("Square =", square)


# ==========================================================
# Question 9
# Convert Celsius to Fahrenheit
# Formula:
# (C × 9/5) + 32
# ==========================================================

celsius = float(input("Enter Temperature in Celsius : "))

fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit =", fahrenheit)


# ==========================================================
# Question 10
# Perform arithmetic operations
# ==========================================================

num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))

print("Addition =", num1 + num2)
print("Subtraction =", num1 - num2)
print("Multiplication =", num1 * num2)
print("Division =", num1 / num2)
print("Floor Division =", num1 // num2)
print("Modulus =", num1 % num2)
print("Power =", num1 ** num2)


# ==========================================================
# END OF DAY 1
#
# Topics Completed
# ✔ print()
# ✔ Variables
# ✔ Data Types
# ✔ Input
# ✔ Output
# ✔ Type Casting
# ✔ Arithmetic Operators
#
# Total Practice Questions : 10
# ==========================================================