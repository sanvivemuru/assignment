# Task 1

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)


n = int(input("Enter n: "))

if n < 0:
    print("Invalid")
else:
    f = fact(n)
    print("Fact is", f)

# Output:
# Enter n: 5
# Fact is 120

#task 2:
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print("First 15 terms:")
for i in range(15):
    print(fibonacci(i), end=" ")

print("\n\nfibonacci(5) is recomputed 5 times while calculating fibonacci(10).")

#output:
#First 15 terms:
#0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 

#fibonacci(5) is recomputed 5 times while calculating fibonacci(10).
    
#task 3:
def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)


def reverse_number(n):
    if n < 10:
        return n
    digits = len(str(n))
    return (n % 10) * (10 ** (digits - 1)) + reverse_number(n // 10)


n = int(input("Enter a number: "))

print("Sum of digits:", sum_of_digits(n))
print("Reversed number:", reverse_number(n))

#output:
#Enter a number: 222
#Sum of digits: 6
#Reversed number: 222

#task 4:
def power(base, exp):
    if exp == 0:
        return 1
    if exp < 0:
        return 1 / power(base, -exp)
    return base * power(base, exp - 1)


base = float(input("Enter base: "))
exp = int(input("Enter exponent: "))

print("Result:", power(base, exp))

#output:
#Enter base: 2
#Enter exponent: 4
#Result: 16.0

#task 5:
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("GCD:", gcd(a, b))
print("LCM:", lcm(a, b))

#output:
#Enter first number: 12
#Enter second number: 24
#GCD: 12
#LCM: 24


#task 6:
def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return

    tower_of_hanoi(n - 1, source, destination, auxiliary)
    print("Move disk", n, "from", source, "to", destination)
    tower_of_hanoi(n - 1, auxiliary, source, destination)


print("For n = 3:")
tower_of_hanoi(3, "A", "B", "C")
print("Total moves:", 2**3 - 1)

print("\nFor n = 4:")
tower_of_hanoi(4, "A", "B", "C")
print("Total moves:", 2**4 - 1)

#output:
#For n = 3:
#Move disk 1 from A to C
#Move disk 2 from A to B
#Move disk 1 from C to B
#Move disk 3 from A to C
#Move disk 1 from B to A
#Move disk 2 from B to C
#Move disk 1 from A to C
#Total moves: 7

#For n = 4:
#Move disk 1 from A to B
#Move disk 2 from A to C
#Move disk 1 from B to C
#Move disk 3 from A to B
#Move disk 1 from C to A
#Move disk 2 from C to B
#Move disk 1 from A to B
#Move disk 4 from A to C
#Move disk 1 from B to C
#Move disk 2 from B to A
#Move disk 1 from C to A
#Move disk 3 from B to C
#Move disk 1 from A to B
#Move disk 2 from A to C
#Move disk 1 from B to C
#Total moves: 15
