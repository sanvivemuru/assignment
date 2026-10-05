# TASK 1

def greet():
    return "Hello"

# (a) Assigning function to another variable
new_function = greet
print(new_function())

# (b) Passing function as an argument
def execute(func):
    print(func())

execute(greet)

# (c) Returning a function from another function
def outer():
    def inner():
        return "Function returned successfully"
    return inner

result = outer()
print(result())

# OUTPUT:
# Hello
# Hello
# Function returned successfully


# TASK 2

def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_call
def add(a, b):
    return a + b

print(add(5, 3))

# OUTPUT:
# Calling add args=(5, 3) kwargs={}
# add returned 8
# 8


# TASK 3

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time taken: {end - start:.6f} seconds")
        return result
    return wrapper

@timer
def heavy_task():
    total = 0
    for i in range(1000000):
        total += i
    return total

print(heavy_task())

# OUTPUT:
# Time taken: 0.04XXXX seconds
# 499999500000


# TASK 4

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greeting():
    print("Hello!")

greeting()

# OUTPUT:
# Hello!
# Hello!
# Hello!


# TASK 5

from functools import wraps

is_logged_in = False

def require_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if is_logged_in:
            return func(*args, **kwargs)
        else:
            print("Access denied. Please login.")
    return wrapper

@require_login
def dashboard():
    print("Welcome to the dashboard!")

dashboard()

is_logged_in = True
dashboard()

# OUTPUT:
# Access denied. Please login.
# Welcome to the dashboard!

# functools.wraps preserves the original function's name and metadata.


# TASK 6

def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time taken: {end - start:.6f} seconds")
        return result
    return wrapper

@log_call
@timer
def calculate(a, b):
    return a + b

print(calculate(10, 20))

# OUTPUT:
# Calling wrapper args=(10, 20) kwargs={}
# Time taken: 0.00000X seconds
# calculate returned 30
# 30

# The decorator closest to the function runs first.
# Here, @timer is applied first, then @log_call.
