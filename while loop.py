# Exercise 8: Print first N natural numbers using while loop
n = int(input("Enter N: "))
i = 1
print("First", n, "natural numbers:")
while i <= n:
    print(i, end=" ")
    i += 1

# Output:
# Enter N: 5
# First 5 natural numbers:
# 1 2 3 4 5

# Exercise 9: Sum and average of digits of a given number
num = int(input("Enter a number: "))
temp = num
sum_digits = 0
count = 0

while temp > 0:
    digit = temp % 10
    sum_digits += digit
    count += 1
    temp = temp // 10

average = sum_digits / count if count > 0 else 0
print("Sum of digits:", sum_digits)
print("Average of digits:", average)

# Output:
# Enter a number: 1234
# Sum of digits: 10
# Average of digits: 2.5


# Exercise 10: Reverse a given integer using while loop
num = int(input("Enter an integer: "))
reversed_num = 0
temp = num

while temp > 0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp = temp // 10

print("Reversed number:", reversed_num)

# Output:
# Enter an integer: 1234
# Reversed number: 4321

# Exercise 11: Check if a number is palindrome using while loop
num = int(input("Enter a number: "))
original_num = num
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10

if original_num == reversed_num:
    print(original_num, "is a palindrome.")
else:
    print(original_num, "is not a palindrome.")

# Output:
# Enter a number: 121
# 121 is a palindrome.

# Exercise 12: Generate Fibonacci series up to N terms
n = int(input("Enter number of terms: "))
a, b = 0, 1
count = 0

print("Fibonacci series:")
while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1

# Output:
# Enter number of terms: 7
# Fibonacci series:
# 0 1 1 2 3 5 8
