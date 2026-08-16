# Exercise 18: Right-angled triangle of stars (N=5)
n = 5
for i in range(1, n+1):
    print('* ' * i)

# Output:
# *
# * *
# * * *
# * * * *
# * * * * *

# Exercise 19: Inverted right-angled triangle of stars (N=5)
n = 5
for i in range(n, 0, -1):
    print('* ' * i)

# Output:
# * * * * *
# * * * *
# * * *
# * *
# *

# Exercise 20: Pyramid (centered triangle) of stars (N=5)
n = 5
for i in range(1, n+1):
    print(' ' * (n-i) + '* ' * i)

# Output:
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

# Exercise 21: Inverted pyramid of stars (N=5)
n = 5
for i in range(n, 0, -1):
    print(' ' * (n-i) + '* ' * i)

# Output:
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

# Exercise 22: Diamond pattern using stars (N=4)
n = 4
# Upper part
for i in range(1, n+1):
    print(' ' * (n-i) + '*' * (2*i-1))
# Lower part
for i in range(n, 0, -1):
    print(' ' * (n-i) + '*' * (2*i-1))

# Output:
#    *
#   ***
#  *****
# *******
# *******
#  *****
#   ***
#    *

# Exercise 23: Number triangle where each row repeats its row number (N=5)
n = 5
for i in range(1, n+1):
    print((str(i) + ' ') * i)

# Output:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# Exercise 24: Number triangle with increasing sequence in each row (N=5)
n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()

# Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


# Exercise 25: Pascal's-Triangle-style pattern (N=5)
n = 5
for i in range(1, n+1):
    # Print increasing numbers
    for j in range(1, i+1):
        print(j, end=' ')
    # Print decreasing numbers
    for j in range(i-1, 0, -1):
        print(j, end=' ')
    print()

# Output:
# 1
# 1 2 1
# 1 2 3 2 1
# 1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1


# Exercise 26: Alphabet pattern (N=5)
n = 5
for i in range(1, n+1):
    # Print alphabets
    for j in range(65, 65+i):
        print(chr(j), end=' ')
    print()

# Output:
# A
# A B
# A B C
# A B C D
# A B C D E

# Exercise 27: Hollow square pattern of stars (N=5)
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

# Output:
# * * * * *
# *       *
# *       *
# *       *
# * * * * *

# Exercise 28: Hollow diamond pattern of stars (N=4)
n = 4
# Upper part
for i in range(1, n+1):
    print(' ' * (n-i) + '* ' * i)
    if i < n:
        print(' ' * (n-i) + '* ' * i)
# Lower part
for i in range(n-1, 0, -1):
    print(' ' * (n-i) + '* ' * i)
    if i > 1:
        print(' ' * (n-i) + '* ' * i)

# Output:
#    *
#   * *
#   * *
#  * * *
#  * * *
# * * * *
# * * * *
#  * * *
#   * *
#    *


# Exercise 29: Floyd's triangle (N=5)
n = 5
num = 1
for i in range(1, n+1):
    for j in range(i):
        print(num, end=' ')
        num += 1
    print()

# Output:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15


# Exercise 30: Butterfly pattern of stars (N=4)
n = 4
# Upper part
for i in range(1, n+1):
    print('* ' * i + ' ' * 2*(n-i) + '* ' * i)
# Middle part
print('* ' * (2*n))
# Lower part
for i in range(n, 0, -1):
    print('* ' * i + ' ' * 2*(n-i) + '* ' * i)

# Output:
# * 
# * *  *
# * * *   *
# * * * *    *
# * * * * * *
# * * * *    *
# * * *   *
# * *  *
# *


