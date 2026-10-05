
'''#A1
#1.
integers = [1,2,3,4,5,6,7,8,9]
for i in range(len(integers)):
    print(integers[i])
print("length of list is :",+len(integers))

#output:1
#2
#3
#4
#5
#6
#7
#8
#9
#length of list is : 9


#2.
list = ['sanvi',10,0.5,['roman'],True]
for i in range(len(list)):
    print(type(list[i]))

#output:<class 'str'>
#<class 'int'>
#<class 'float'>
#<class 'list'>
#<class 'bool'>

#3.
a = []
a.append(10)
a.append(12)
a.append('sanvi')
a.append(0.5)
a.append(True)
for i in range(len(a)):
    print(a[i])

#output:
#10
#12
#sanvi
#0.5
#True

#4.
fruits = ['apple','banana','orange','pineapple','watermelon','grapes','pomogranate','plum']
print(fruits[0],fruits[7],fruits[3])

#output: apple plum pineapple

#5.
a = input("enter list: ").split()


for i,val in enumerate(a):
    print(i,",",val)
#output:
#enter list: 10 20 30 
#0 , 10
#1 , 20
#2 , 30

#6.
a = input("enter list: ").split()
n = len(a)
print("first 3 elements: ",a[0:3])
print("last 3 elements: ",a[-4:-1])
print("alternate elements: ",a[::2])

#output:
#enter list: 1 2 3 4 5 6 7 8 9
#first 3 elements:  ['1', '2', '3']
#last 3 elements:  ['6', '7', '8']
#alternate elements:  ['1', '3', '5', '7', '9']

#7.
a = [1,2,3,4,5,6]
print('original list: ',a[:])
print('reversed list: ',a[::-1])

#output:
#original list:  [1, 2, 3, 4, 5, 6]
#reversed list:  [6, 5, 4, 3, 2, 1]

#8.
a = [1,2,3,4,5,6,7,8,9,10,11,12]
print(a[4:8])

#output:
#[5, 6, 7, 8]

#9.
a = input("enter list of 7 elements: ").split()
print("last element:",a[-1])
print("second last element:",a[-2])
print("last 3 elements:",a[-3:])

#output:
#enter list of 7 elements: 1 2 3 4 5 6 7 8 9
#last element: 9
#second last element: 8
#last 3 elements: ['7', '8', '9']

#10.
a = input("enter list: ").split()
print('reverse list:',a[::-1])

#output:
#enter list: 10 20 50 44
#reverse list: ['44', '50', '20', '10']

#11.
a = [5,22,33,44,55,66,77]
a.append(10)
print('list after appending:',a[:])
a.insert(1,5)
print('list after insertion:',a[:])
a.extend([8,9,11])
print('list after extend:',a[:])
a.remove(10)
print('list after removal:',a[:])
a.pop()
print('list after pop:',a[:])
a.sort()
print('list after sorting:',a[:])
a.reverse()
print('list after reverse:',a[:])
print(a.count(5))
print(a.index(44))

#output:
#list after appending: [5, 22, 33, 44, 55, 66, 77, 10]
#list after insertion: [5, 5, 22, 33, 44, 55, 66, 77, 10]
#list after extend: [5, 5, 22, 33, 44, 55, 66, 77, 10, 8, 9, 11]
#list after removal: [5, 5, 22, 33, 44, 55, 66, 77, 8, 9, 11]
#list after pop: [5, 5, 22, 33, 44, 55, 66, 77, 8, 9]
#list after sorting: [5, 5, 8, 9, 22, 33, 44, 55, 66, 77]
#list after reverse: [77, 66, 55, 44, 33, 22, 9, 8, 5, 5]
#2
#3

#12.
import ast

a = ast.literal_eval(input("enter list: "))
unique = []
for item in a:
    if item not in unique:
        unique.append(item)
print(unique)
'''

#13
a = input("enter list: ").split()
min = a[0]
for i in range(len(a)):
    if(a[i]<min):
        min = a[i]
max = a[0]
for i in range(len(a)):
    if(a[i]>max):
        max = a[i]
sum = 0
for i in range(len(a)):
    sum = sum+a[i]
print("min is %d"+min)
print("max is %d"+max)
print("sum is %d"+sum)
