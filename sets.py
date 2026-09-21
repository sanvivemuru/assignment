# 1

s = {1, 2, 3, 4, 4, 5, 5, 6}
print(s)

# Output:
# {1, 2, 3, 4, 5, 6}


# 2

my_list = [1, 2, 2, 3, 4, 4]
my_string = "hello"

print(set(my_list))
print(set(my_string))

# Output:
# {1, 2, 3, 4}
# {'h', 'e', 'l', 'o'}


# 3

s = {1, 2, 3}

s.add(4)
s.update([5, 6, 7])

print(s)

# Output:
# {1, 2, 3, 4, 5, 6, 7}


# 4

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Union:", A.union(B))
print("Intersection:", A.intersection(B))
print("Difference:", A.difference(B))
print("Symmetric Difference:", A.symmetric_difference(B))

# Output:
# Union: {1, 2, 3, 4, 5, 6}
# Intersection: {3, 4}
# Difference: {1, 2}
# Symmetric Difference: {1, 2, 5, 6}


# 5

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}

print(A.issubset(B))
print(B.issuperset(A))

# Output:
# True
# True


# 6

s = {1, 2, 3, 4}

s.remove(2)
s.discard(5)

print(s)

# Output:
# {1, 3, 4}


# 7

A = {1, 2, 3}
B = {4, 5, 6}

print(A.isdisjoint(B))

# Output:
# True


# 8

numbers = [5, 2, 3, 2, 5, 1, 4, 3]

unique_numbers = set(numbers)
sorted_numbers = sorted(unique_numbers)

print(unique_numbers)
print(sorted_numbers)

# Output:
# {1, 2, 3, 4, 5}
# [1, 2, 3, 4, 5]


# 9

squares = {x ** 2 for x in range(1, 21) if x % 2 != 0}

print(squares)

# Output:
# {1, 9, 25, 49, 81, 121, 169, 225, 289, 361}
