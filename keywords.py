import keyword
print(keyword.kwlist)
#output:['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else',
#'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

class Check:
 import keyword
 string = input("enter a string: ")
 if keyword.iskeyword(string):
  print("given string is a keyword")
 else:
  print("given string is not a keyword")
#output:enter a string: hello
#given string is not a keyword

class var:
 for = 5
 True = 10
 print(for)
 print(True)
#output: INVALID SYNTAX
 
