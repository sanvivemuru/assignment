# TASK 1

def to_fahrenheit(c):
    return (c * 9/5) + 32

temperatures = [0, 10, 20, 30, 40]
result = list(map(to_fahrenheit, temperatures))
print(result)

words = ["hello", "python", "world"]
result = list(map(str.upper, words))
print(result)

# OUTPUT:
# [32.0, 50.0, 68.0, 86.0, 104.0]
# ['HELLO', 'PYTHON', 'WORLD']


# TASK 2

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = list(range(1, 51))
primes = list(filter(is_prime, numbers))
print(primes)

words = ["madam", "hello", "level", "python", "radar"]
palindromes = list(filter(lambda x: x == x[::-1], words))
print(palindromes)

# OUTPUT:
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
# ['madam', 'level', 'radar']


# TASK 3

from functools import reduce

numbers = [2, 3, 4, 5]

product = reduce(lambda a, b: a * b, numbers)
print(product)

maximum = reduce(lambda a, b: a if a > b else b, numbers)
print(maximum)

words = ["Python", "is", "easy", "to", "learn"]
sentence = reduce(lambda a, b: a + " " + b, words)
print(sentence)

# OUTPUT:
# 120
# 5
# Python is easy to learn


# TASK 4

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = filter(lambda x: x % 2 == 0, nums)
squares = map(lambda x: x ** 2, evens)
total = reduce(lambda a, b: a + b, squares)

print(total)

total2 = sum([x ** 2 for x in nums if x % 2 == 0])
print(total2)

# OUTPUT:
# 220
# 220


# TASK 5

employees = [
    {"name": "Amit", "department": "CSE", "salary": 30000},
    {"name": "Ravi", "department": "ECE", "salary": 25000},
    {"name": "Priya", "department": "CSE", "salary": 40000},
    {"name": "Sneha", "department": "ECE", "salary": 35000},
    {"name": "Rahul", "department": "CSE", "salary": 20000}
]

cse_employees = list(filter(
    lambda e: e["department"] == "CSE", employees
))

def salary_hike(employee):
    return {
        "name": employee["name"],
        "department": employee["department"],
        "salary": employee["salary"] * 1.10
    }

updated_employees = list(map(salary_hike, cse_employees))
print(updated_employees)

total_salary = reduce(
    lambda a, b: a + b["salary"],
    updated_employees,
    0
)

print(total_salary)

# OUTPUT:
# [{'name': 'Amit', 'department': 'CSE', 'salary': 33000.0}, {'name': 'Priya', 'department': 'CSE', 'salary': 44000.0}, {'name': 'Rahul', 'department': 'CSE', 'salary': 22000.0}]
# 99000.0
