class Variables:
 name = "sanvi"
 age = 18
 height = 162.5
 student = True
 print("Name:",name,"type:",type(name))
 print("Age:",age,"type:",type(age))
 print("Height:",height,"type:",type(height))
 print("Student Status:",student,"type:",type(student))
 
#output: Name: sanvi type: <class 'str'>
#Age: 18 type: <class 'int'>
#Height: 162.5 type: <class 'float'>
#Student Status: True type: <class 'bool'>

class Assign:
 a,b,c = 10,20,30
 a=b=c=100
 print(a),print(b),print(c)

#output: 100
#        100
#        100

class Swap1:
 a,b = 10,20
 a,b = b,a
 print(a,b)

#output: 20 10

class Swap2:
 a,b = 10,20
 c=a
 a=b
 b=c
 print(a,b)

#output: 20 10

class Dynamic:
 a = 5
 print(a,type(a))
 a = "hello"
 print(a,type(a))

#output: 5 <class 'int'>
#        hello <class 'str'>

 
