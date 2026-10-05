
# TASK 1: 


counter = 0

def show_local():
    counter = 10
    print("Local counter:", counter)

show_local()
print("Global counter:", counter)

# OUTPUT:
# Local counter: 10
# Global counter: 0



# TASK 2: 

def increment_counter():
    global counter
    counter = counter + 1

print("\nTask 2:")
for i in range(5):
    increment_counter()
    print("Counter:", counter)

# OUTPUT:
# Counter: 1
# Counter: 2
# Counter: 3
# Counter: 4
# Counter: 5


# TASK 3:

counter = 0

def wrong_increment():
    counter = counter + 1
    print(counter)

print("\nTask 3:")
try:
    wrong_increment()
except UnboundLocalError:
    print("UnboundLocalError occurred")

# OUTPUT:
# UnboundLocalError occurred


# FIXED FUNCTION USING global KEYWORD

def correct_increment():
    global counter
    counter = counter + 1
    print("Counter after fixing:", counter)

correct_increment()

# OUTPUT:
# Counter after fixing: 1


# TASK 4:

def make_counter():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        return count

    return increment

my_counter = make_counter()

print("\nTask 4:")
print(my_counter())
print(my_counter())
print(my_counter())
print(my_counter())

# OUTPUT:
# 1
# 2
# 3
# 4


# TASK 5: Bank Account Simulation

balance = 1000

def deposit(amount):
    global balance
    balance = balance + amount
    print("Amount deposited:", amount)

def withdraw(amount):
    global balance

    if amount <= balance:
        balance = balance - amount
        print("Amount withdrawn:", amount)
    else:
        print("Insufficient funds")

def check_balance():
    print("Current balance:", balance)


print("\nTask 5:")

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = int(input("Enter deposit amount: "))
        deposit(amount)

    elif choice == 2:
        amount = int(input("Enter withdrawal amount: "))
        withdraw(amount)

    elif choice == 3:
        check_balance()

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice")

# SAMPLE OUTPUT:
#
# 1. Deposit
# 2. Withdraw
# 3. Check Balance
# 4. Exit
# Enter your choice: 3
# Current balance: 1000
#
# 1. Deposit
# 2. Withdraw
# 3. Check Balance
# 4. Exit
# Enter your choice: 1
# Enter deposit amount: 500
# Amount deposited: 500
#
# 1. Deposit
# 2. Withdraw
# 3. Check Balance
# 4. Exit
# Enter your choice: 2
# Enter withdrawal amount: 200
# Amount withdrawn: 200
#
# 1. Deposit
# 2. Withdraw
# 3. Check Balance
# 4. Exit
# Enter your choice: 3
# Current balance: 1300
#
# 1. Deposit
# 2. Withdraw
# 3. Check Balance
# 4. Exit
# Enter your choice: 4
# Thank you!
