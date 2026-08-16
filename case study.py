#case study 1:
cost = 250
n = int(input("enter no of people: "))
price = cost*n
print("price without discount : ",price)
if(price>500):
    final_price = price-100
    print("final price is ",final_price)
else:
    print("discount not applicable")

#output:enter no of people: 4
#price without discount :  1000
#final price is  900


#case study 2:
first_name = str(input("enter your first name: "))
roll_number = input("enter your roll no: ")
print("username is ",first_name.lower()+roll_number[-2].lower()+roll_number[-1].lower())

#output:enter your first name: sanvi
#enter your roll no: 25341A05N2
#username is  sanvin2


#case study 3:
balance = 10000
amount = int(input("enter amount: "))
if(amount<=balance and amount%100==0):
    print("success")
elif(amount>balance):
    print("not enough balance")
else:
    print("invalid")

#output:enter amount: 4500
#success

#case study 4:
salary = input(int("enter salary: "))
salary1 = print(salary+=salary
