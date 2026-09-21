# 1

import re

sentence = "1024 requests were served in 3 seconds"

result = re.match(r"\d", sentence)

if result:
    print("Sentence starts with a digit")
else:
    print("Sentence does not start with a digit")

# Output:
# Sentence starts with a digit


# 2

result = re.search(r"served", sentence)

if result:
    print("Start and end position:", result.span())

# Output:
# Start and end position: (22, 28)


# 3

s1 = "12345"
s2 = "123a5"

print(re.fullmatch(r"\d+", s1))
print(re.fullmatch(r"\d+", s2))

# Output:
# <re.Match object; span=(0, 5), match='12345'>
# None


# 4

# match() checks only the beginning of the string, so it succeeds if the
# pattern matches at the start. fullmatch() checks the entire string,
# so it fails when other characters are present later.

#TASK 2
# 1

import re

text = "NASA and USA are working together. ISRO is also collaborating with NASA."

capital_words = re.findall(r"\b[A-Z]{2,}\b", text)

print(capital_words)

# Output:
# ['NASA', 'USA', 'ISRO', 'NASA']


# 2

for match in re.finditer(r"\b[A-Za-z]{7,}\b", text):
    print(match.group(), match.start())

# Output:
# working 13
# together 21
# collaborating 48


# 3

prices = "apples: $3.50, bananas: $1.20, mango: $4.75"

amounts = re.findall(r"\$\d+\.\d+", prices)

print(amounts)

# Output:
# ['$3.50', '$1.20', '$4.75']


# 4

print("Number of dollar amounts:", len(amounts))

# Output:
# Number of dollar amounts: 3

#TASK 3
# 1

import re

def redact_emails(text):
    return re.sub(r'\b[\w.-]+@[\w.-]+\.\w+\b', '[EMAIL HIDDEN]', text)

text = "Contact john@gmail.com or admin@example.com for help."
print(redact_emails(text))

# Output:
# Contact [EMAIL HIDDEN] or [EMAIL HIDDEN] for help.


# 2

names = "Doe, John"

result = re.sub(r'(\w+),\s*(\w+)', r'\2 \1', names)

print(result)

# Output:
# John Doe


# 3

def double_numbers(match):
    return str(int(match.group()) * 2)

text = "I have 3 apples and 5 oranges."

result = re.sub(r'\d+', double_numbers, text)

print(result)

# Output:
# I have 6 apples and 10 oranges.


# 4

text = "Wait!!! What??? Really!!!"

result, count = re.subn(r'([!?])\1+', r'\1', text)

print(result)
print("Replacements:", count)

# Output:
# Wait! What? Really!
# Replacements: 3

