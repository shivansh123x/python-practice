# make a calculator
"""
while True:
    print("1. addition")
    print("2.substraction")
    print("3.divide")
    print("4.multiply")
    print("5.exit")

    num1=int(input("enter the first number"))
    num2=int(input("enter the second number"))
    choice=int(input("enter your choice"))
    
    if choice==1:
        print(num1+num2)
    elif choice==2:
        print(num2-num1)
    elif choice==3:
        print(num1/num2)
    elif choice==4:
        print(num1*num2)
    elif choice==5:
        print("exited")
        break
        
    else:
        print("invalid input")

    """




# word frequency counter
"""
data=str(input("Enter the string pleaase:"))
count=0
search=str(input("Enter the word you want to search:"))

for i in data.split():
    if i==search:
        count=count+1
    print(f" {i} have repeated {count} times")
"""

# project - to calculate expense

mylist=[]
total_amount=[]
while True:
    print("1.to add more ")
    print("2. to end")
    
    category=str(input("Enter the item name:"))
    amount=int(input("Enter the amount you spent"))
    choice=int(input("Enter the choice:"))
    list1=[category,amount]
    total_amount.append(amount)

    if choice==1:
        mylist.append(list1)
        print(mylist)
        print("total amount spent:",sum(total_amount))
    elif choice==2:
        print("closed")
        mylist.append(list1)
        print(mylist)
        print("total amount spent:",sum(total_amount))
        break
    














