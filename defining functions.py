#task 01:
def greet(name):
    print(f"Hello {name}! welcome to python")
greet("sanvi")
greet("asha")
greet("ravi")

#output:
#Hello sanvi! welcome to python
#Hello asha! welcome to python
#Hello ravi! welcome to python

#task 02:
def simple_interest(principal,rate,time):
    si = (principal*rate*time)/100
    print(f"simple interest is {si}")
p = float(input("enter principal: "))
r = float(input("enter rate: "))
t = float(input("enter time: "))
simple_interest(p,r,t)

#output:
#enter principal: 200
#enter rate: 10
#enter time: 3
#simple interest is 60.0

#task 03:
def is_even(n):
    return n%2 == 0
for i in range(5):
    n = int(input("enter n: "))
    if is_even(n):
        print("even")
    else:
        print("odd")

#output:
#enter n: 3
#odd
#enter n: 4
#even
#enter n: 5
#odd
#enter n: 12
#even
#enter n: 122
#even

#task 04:
def stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)

    return minimum, maximum, average


numbers = [10, 20, 30, 40, 50]

minimum, maximum, average = stats(numbers)

print("Minimum:", minimum)
print("Maximum:", maximum)
print("Average:", average)

#output:
#Minimum: 10
#Maximum: 50
#Average: 30.0

#task 05:
def celsius_to_fahrenheit(c):
     f=((9/5)*c) + 32
     return f
def reverse(f):
     c = (f-32)*5/9
     return c
while True:
    print("MENU")
    print("1.celcius to fahrenheit")
    print("2.fahrenheit to celcius")
    print("3.exit")
    choice = int(input("enter choice: "))
    match choice:
     case 1:
        cel = int(input("enter temp in celcius: "))
        f = celsius_to_fahrenheit(cel)
        print(f"fahrenheit: {f}")
     case 2:
        f1 = int(input("enter temp in fahrenheit: "))
        c = reverse(f1)
        print(f"celcius: {c}")
     case 3:
        print("exiting..")
        break
     case _:
        print("invalid choice")

        
#output:
#MENU
#1.celcius to fahrenheit
#2.fahrenheit to celcius
#3.exit
#enter choice: 1
#enter temp in celcius: 200
#fahrenheit: 392.0

            
    
