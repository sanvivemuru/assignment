#task 1:
# (a) Square of a number
square = lambda x: x * x

# (b) Check if a number is even
is_even = lambda x: x % 2 == 0

# (c) Larger of two numbers
larger = lambda a, b: a if a > b else b

print(square(5))
print(is_even(8))
print(larger(10, 7))

# Output:
# 25
# True
# 10

#task 2:
grade = lambda marks: "Pass" if marks >= 40 else "Fail"

marks_list = [25, 40, 56, 32, 78, 39]

for marks in marks_list:
    print(marks, grade(marks))

# Output:
# 25 Fail
# 40 Pass
# 56 Pass
# 32 Fail
# 78 Pass
# 39 Fail

#task 3:
students = [("Ravi", 78), ("Sita", 92), ("Amit", 65)]

sorted_students = sorted(students, key=lambda s: s[1], reverse=True)
print(sorted_students)

names = ["Ravi", "Sita", "Amit", "Krishna"]

sorted_names = sorted(names, key=lambda x: len(x))
print(sorted_names)

# Output:
# [('Sita', 92), ('Ravi', 78), ('Amit', 65)]
# ['Ravi', 'Sita', 'Amit', 'Krishna']

#task 4:
numbers = [1, 2, 3, 4, 6, 9]

cubes = list(map(lambda x: x ** 3, numbers))
print(cubes)

divisible_by_3 = list(filter(lambda x: x % 3 == 0, numbers))
print(divisible_by_3)

# Output:
# [1, 8, 27, 64, 216, 729]
# [3, 6, 9]

