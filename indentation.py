class IndentationErrorDemo:
    def run(self):
        x = 10
        if x > 5:
            print("x is greater than 5")
            print("This line has inconsistent indentation (mixing tabs and spaces)")
        else:
            print("x is 5 or less")

# Output (when run):
# IndentationError: expected an indented block




class NestedLoopEvenOdd:
    def run(self):
        for num in range(1, 11):
            if num % 2 == 0:
                print(f"{num} is Even")
            else:
                print(f"{num} is Odd")

# Output:
# 1 is Odd
# 2 is Even
# 3 is Odd
# 4 is Even
# 5 is Odd
# 6 is Even
# 7 is Odd
# 8 is Even
# 9 is Odd
# 10 is Even


#FOR i FROM 1 TO 5
#   IF i == 3
#PRINT "Middle"
#   ELSE
#       PRINT i
#   END IF
#END FOR

class PseudocodeRewrite:
    def run(self):
        for i in range(1, 6):
            if i == 3:
                print("Middle")
            else:
                print(i)

# Output:
# 1
# 2
# Middle
# 4
# 5
