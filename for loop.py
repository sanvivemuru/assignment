# Exercise 13: Print multiplication table of a given number
num = int(input("Enter a number: "))
print(f"Multiplication table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Output:
# Enter a number: 5
# Multiplication table of 5:
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50

# Exercise 14: Find factorial of a given number
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"Factorial of {num} is {factorial}")

# Output:
# Enter a number: 5
# Factorial of 5 is 120


# Exercise 15: Count vowels, consonants, digits, and spaces in a string
text = input("Enter a string: ")
vowels = consonants = digits = spaces = 0
vowel_set = {'a', 'e', 'i', 'o', 'u'}

for char in text.lower():
    if char.isalpha():
        if char in vowel_set:
            vowels += 1
        else:
            consonants += 1
    elif char.isdigit():
        digits += 1
    elif char == ' ':
        spaces += 1

print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Digits: {digits}")
print(f"Spaces: {spaces}")

# Output:
# Enter a string: Hello World 123
# Vowels: 3
# Consonants: 7
# Digits: 3
# Spaces: 2


# Exercise 16: Check if a number is prime
num = int(input("Enter a number: "))
if num > 1:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    print(f"{num} is a prime number." if is_prime else f"{num} is not a prime number.")
else:
    print(f"{num} is not a prime number.")

# Output:
# Enter a number: 17
# 17 is a prime number.


# Exercise 17: Print all prime numbers between two limits
start = int(input("Enter start limit: "))
end = int(input("Enter end limit: "))
print(f"Prime numbers between {start} and {end}:")

for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")

# Output:
# Enter start limit: 10
# Enter end limit: 30
# Prime numbers between 10 and 30:
# 11 13 17 19 23 29

