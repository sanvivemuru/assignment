# 1

s = input("Enter a string: ")
print(len(s))

# Output:
# Enter a string: Hello
# 5


# 2

s = input("Enter a string: ")

rev = ""
for i in range(len(s) - 1, -1, -1):
    rev += s[i]

print("Without slicing:", rev)
print("With slicing:", s[::-1])

# Output:
# Enter a string: Hello
# Without slicing: olleH
# With slicing: olleH


# 3

s = input("Enter a string: ")

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

# Output:
# Enter a string: madam
# Palindrome


# 4

s = input("Enter a string: ")

print("Uppercase:", s.upper())
print("Lowercase:", s.lower())

# Output:
# Enter a string: Hello World
# Uppercase: HELLO WORLD
# Lowercase: hello world


# 5

s = input("Enter a string: ")

vowels = consonants = digits = spaces = 0

for ch in s:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)

# Output:
# Enter a string: Hello 123
# Vowels: 2
# Consonants: 3
# Digits: 3
# Spaces: 1


# 6

s = input("Enter a string: ")
ch = input("Enter character: ")

print("Occurrences:", s.count(ch))

# Output:
# Enter a string: banana
# Enter character: a
# Occurrences: 3


# 7

s = input("Enter a string: ")

print(s.replace(" ", ""))

# Output:
# Enter a string: Hello World Python
# HelloWorldPython


# 8

s = input("Enter a string: ")
old = input("Enter word to replace: ")
new = input("Enter new word: ")

print(s.replace(old, new))

# Output:
# Enter a string: I like Java
# Enter word to replace: Java
# Enter new word: Python
# I like Python


# 9

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

print("".join([s1, s2]))

# Output:
# Enter first string: Hello
# Enter second string: World
# HelloWorld


# 10

s = input("Enter a string: ")

print(s.swapcase())

# Output:
# Enter a string: Hello WORLD
# hELLO world


# 11

s = input("Enter a string: ")

print("First character:", s[0])
print("Last character:", s[-1])

# Output:
# Enter a string: Python
# First character: P
# Last character: n


# 12

s = input("Enter a string: ")

print(s[::2])

# Output:
# Enter a string: Python
# Pto


# 13

s = input("Enter a string: ")
sub = input("Enter substring: ")

if sub in s:
    print("Substring exists")
else:
    print("Substring does not exist")

# Output:
# Enter a string: Hello Python
# Enter substring: Python
# Substring exists


# 14

s = input("Enter a string: ")
ch = input("Enter character: ")

first = s.find(ch)
last = s.rfind(ch)

print("First occurrence:", first)
print("Last occurrence:", last)

# Output:
# Enter a string: banana
# Enter character: a
# First occurrence: 1
# Last occurrence: 5


# 15

s = input("Enter a sentence: ")

words = s.split()
print("Number of words:", len(words))

# Output:
# Enter a sentence: Python is easy to learn
# Number of words: 5


# 16

s = input("Enter a sentence: ")

words = s.split()
longest = max(words, key=len)

print("Longest word:", longest)

# Output:
# Enter a sentence: Python is very interesting
# Longest word: interesting


# 17

s = input("Enter a sentence: ")

words = s.split()
print(" ".join(words[::-1]))

# Output:
# Enter a sentence: I love Python
# Python love I


# 18

s = input("Enter a sentence: ")

words = s.split()
result = ""

for word in words:
    result += word[0].upper() + word[1:].lower() + " "

print(result.strip())

# Output:
# Enter a sentence: hello world python
# Hello World Python


# 19

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if sorted(s1.lower()) == sorted(s2.lower()):
    print("Anagrams")
else:
    print("Not anagrams")

# Output:
# Enter first string: listen
# Enter second string: silent
# Anagrams


# 20

s = input("Enter a string: ")

result = ""

for ch in s:
    if ch not in result:
        result += ch

print(result)

# Output:
# Enter a string: programming
# progamin


# 21

s = input("Enter a string: ")

if s.isdigit():
    print("Only digits")
elif s.isalpha():
    print("Only alphabets")
elif s.isalnum():
    print("Alphanumeric")
else:
    print("Other characters")

# Output:
# Enter a string: Python123
# Alphanumeric


# 22

s = input("Enter a string: ")

for ch in set(s):
    count = s.count(ch)
    if count > 1:
        print(ch, ":", count)

# Output:
# Enter a string: programming
# r : 2
# g : 2
# m : 2


# 23

s = input("Enter a string: ")

char_list = list(s)
print("List:", char_list)

new_string = "".join(char_list)
print("String:", new_string)

# Output:
# Enter a string: Hello
# List: ['H', 'e', 'l', 'l', 'o']
# String: Hello


# 24

s = input("Enter an identifier: ")

if s.isidentifier():
    print("Valid identifier")
else:
    print("Invalid identifier")

# Output:
# Enter an identifier: student_name
# Valid identifier


# 25

s = input("Enter a string: ")
sub = input("Enter substring: ")

# Own version of find()
index = -1

for i in range(len(s) - len(sub) + 1):
    if s[i:i + len(sub)] == sub:
        index = i
        break

# Own version of count()
count = 0

for i in range(len(s) - len(sub) + 1):
    if s[i:i + len(sub)] == sub:
        count += 1

print("Find:", index)
print("Count:", count)

# Output:
# Enter a string: banana
# Enter substring: an
# Find: 1
# Count: 2
