#B1
a=23
b=6
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)


#output:29
#17
#138
#3.8333333333333335
#3
#5
#148035889

#B2
m = int(input("enter m: "))
n = int(input("enter n: "))
print(m==n)
print(m!=n)
print(m>n)
print(m<n)
print(m>=n)
print(m<=n)


#output: enter m: 5
#enter n: 22
#False
#True
#False
#True
#False
#True

#B3
score = 50
print(score)
score += 10
print(score)
score -= 5
print(score)
score *= 2
print(score)
score /= 4
print(score)
score //= 3
print(score)
score %= 4
print(score)
score **= 3
print(score)

#output:50
#60
#55
#110
#27.5
#9.0
#1.0
#1.0

#B4
percentage = float(input("Enter percentage: "))
attendance = float(input("Enter attendance %: "))
eligible = percentage > 75 and attendance > 90
print("Eligible for scholarship:", eligible)

#output:Enter percentage: 22
#Enter attendance %: 65
#Eligible for scholarship: False


#B5
p = 12
q = 10
print(bin(p),bin(q))
print(p&q)
print(p|q)
print(p^q)
print(~p)
print(p<<2)
print(p>>2)

#output:0b1100 0b1010
#8
#14
#6
#-13
#48
#3

#B6
fruits = ["apple", "banana", "mango", "grape", "kiwi"]
item = input("Enter a fruit: ")
print(item, "is in the list:", item in fruits)
print(item, "is not in the list:", item not in fruits)

#output:Enter a fruit: hello
#hello is in the list: False
#hello is not in the list: True


#B7
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("list1 is list2:", list1 is list2)
print("list1 is list3:", list1 is list3)
print("list2 is list3:", list2 is list3)

print("\nid(list1):", id(list1))
print("id(list2):", id(list2))
print("id(list3):", id(list3))

#output:list1 is list2: False
#list1 is list3: True
#list2 is list3: False

#id(list1): 2686781520256
#id(list2): 2686737641344
#id(list3): 2686781520256

