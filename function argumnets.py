# TASK 1: Positional and Keyword Arguments

def student_info(name, roll_no, branch):
    print("Name:", name)
    print("Roll No:", roll_no)
    print("Branch:", branch)


# Positional arguments
student_info("Sanvi", 101, "CSE")

# Keyword arguments in different order
student_info(branch="CSE", name="Sanvi", roll_no=101)

# Output:
# Name: Sanvi
# Roll No: 101
# Branch: CSE
# Name: Sanvi
# Roll No: 101
# Branch: CSE


# TASK 2: Default Arguments

def calculate_price(price, tax_rate=18, discount=0):
    tax = price * tax_rate / 100
    total = price + tax - discount
    return total


print("\nTask 2:")
print(calculate_price(1000))
print(calculate_price(1000, 10))
print(calculate_price(1000, 10, 100))

# Output:
# Task 2:
# 1180.0
# 1100.0
# 1000.0


# TASK 3: Variable-Length Arguments (*args)

def total_marks(*marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average


print("\nTask 3:")
print(total_marks(80, 85, 90))
print(total_marks(75, 80, 85, 90, 95))
print(total_marks(88))

# Output:
# Task 3:
# (255, 85.0)
# (425, 85.0)
# (88, 88.0)


# TASK 4: Keyword Variable-Length Arguments (**kwargs)

def build_profile(**details):
    print("\n--- Profile Card ---")
    for key, value in details.items():
        print(key.capitalize() + ":", value)


build_profile(name="Sanvi", age=19, city="Hyderabad", hobby="Drawing")

build_profile(name="Ravi", branch="CSE", hobby="Coding")

# Output:
# --- Profile Card ---
# Name: Sanvi
# Age: 19
# City: Hyderabad
# Hobby: Drawing
#
# --- Profile Card ---
# Name: Ravi
# Branch: CSE
# Hobby: Coding


# TASK 5: Combining All Argument Types

def order_summary(customer, *items, discount=0, **extra):
    print("\n--- Order Summary ---")
    print("Customer:", customer)

    print("Items:")
    for item in items:
        print("-", item)

    print("Discount:", discount)

    print("Extra Information:")
    for key, value in extra.items():
        print(key.replace("_", " ").capitalize() + ":", value)


order_summary(
    "Sanvi",
    "Crochet Bag",
    "Keychain",
    "Flower",
    discount=100,
    delivery_address="Hyderabad",
    gift_wrap="Yes"
)

# Output:
# --- Order Summary ---
# Customer: Sanvi
# Items:
# - Crochet Bag
# - Keychain
# - Flower
# Discount: 100
# Extra Information:
# Delivery address: Hyderabad
# Gift wrap: Yes
