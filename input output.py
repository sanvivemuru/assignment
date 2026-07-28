class GreetingProgram:
    def run(self):
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        print(f"Hello {name}, you will turn {age + 1} next year.")

# Output:
# Enter your name: sanvi
# Enter your age: 18
# Hello sanvi, you will turn 18 next year.



class ArithmeticOperations:
    def run(self):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"Sum: {num1 + num2}")
        print(f"Difference: {num1 - num2}")
        print(f"Product: {num1 * num2}")
        print(f"Quotient: {num1 / num2}")

# Output:
# Enter first number: 10
# Enter second number: 5
# Sum: 15.0
# Difference: 5.0
# Product: 50.0
# Quotient: 2.0



class OutputFormattingDemo:
    def run(self):
        name = "Bob"
        marks = 85.5

    
        print("Using comma-separated print():", name, marks)


        print("Using str.format(): {}".format(name))
        print("Using str.format() with marks: {:.2f}".format(marks))

        print(f"Using f-strings: Name = {name}, Marks = {marks}")

# Output:
# Using comma-separated print(): Bob 85.5
# Using str.format(): Bob
# Using str.format() with marks: 85.50
# Using f-strings: Name = Bob, Marks = 85.5


class SumOfMultipleValues:
    def run(self):
        input_values = input("Enter numbers separated by spaces: ")
        numbers = list(map(int, input_values.split()))
        print(f"Sum: {sum(numbers)}")

# Output:
# Enter numbers separated by spaces: 10 20 30
# Sum: 60

