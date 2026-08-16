# Exercise 1: Check if a number is positive, negative, or zero
num = float(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# Output:
# Enter a number: 5
# The number is positive.


# Exercise 2: Check if a year is a leap year
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# Output:
# Enter a year: 2024
# 2024 is a leap year.


# Exercise 3: Check the type of triangle
a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("It is an equilateral triangle.")
    elif a == b or b == c or a == c:
        print("It is an isosceles triangle.")
    else:
        print("It is a scalene triangle.")
else:
    print("It is not a valid triangle.")

# Output:
# Enter side 1: 5
# Enter side 2: 5
# Enter side 3: 5
# It is an equilateral triangle.


# Exercise 4: Find the largest of three numbers using nested if-else
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b:
    if a >= c:
        print(f"{a} is the largest.")
    else:
        print(f"{c} is the largest.")
else:
    if b >= c:
        print(f"{b} is the largest.")
    else:
        print(f"{c} is the largest.")

# Output:
# Enter first number: 10
# Enter second number: 20
# Enter third number: 15
# 20.0 is the largest.

# Exercise 5: Find the grade based on marks
marks = float(input("Enter student's marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
else:
    print("Grade: F")

# Output:
# Enter student's marks: 85
# Grade: B

# Exercise 6: Check if a character is a vowel, consonant, digit, or special symbol
char = input("Enter a character: ")

if char.isalpha():
    if char.lower() in 'aeiou':
        print("It is a vowel.")
    else:
        print("It is a consonant.")
elif char.isdigit():
    print("It is a digit.")
else:
    print("It is a special symbol.")

# Output:
# Enter a character: a
# It is a vowel.


# Exercise 7: Check if a date is valid
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

if month < 1 or month > 12:
    print("Invalid month.")
elif day < 1:
    print("Invalid day.")
else:
    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_days = 31
    elif month in [4, 6, 9, 11]:
        max_days = 30
    else:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            max_days = 29
        else:
            max_days = 28
    if day > max_days:
        print("Invalid day for the given month and year.")
    else:
        print("The date is valid.")

# Output:
# Enter year: 2024
# Enter month: 2
# Enter day: 29
# The date is valid.



