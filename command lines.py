# greet.py
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python greet.py <name>")
        return
    name = sys.argv
    print(f"Hello, {name}!")

if __name__ == "__main__":
    main()


# sum.py
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python sum.py <number1> <number2>")
        return
    try:
        num1 = int(sys.argv)
        num2 = int(sys.argv)
        print(f"Sum: {num1 + num2}")
    except ValueError:
        print("Error: Both arguments must be integers.")

if __name__ == "__main__":
    main()


#output: Sum: 12


# args_info.py
import sys

def main():
    print(f"Script name: {sys.argv}")
    print(f"Total arguments passed: {len(sys.argv) - 1}")

if __name__ == "__main__":
    main()
