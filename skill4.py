# palindrome word

def palindrome(word):
    if word==word[::-1]:
        return True
    return False

print(palindrome("racecar"))



# simple interest

def interest():

    P=int(input("Enter the principle amount:"))
    R=int(input("Enter the rate:"))
    T=int(input("Enter the time period(in years):"))

    simple_interest=(P*R*T)/100

    print(f"simple interest: {simple_interest} rupees")

    total_amount=P*(1+R*T)

    print(f"total amount after interest: {total_amount} rupees")
interest()




#contact book

contacts=[]
while True:
    print("1.to add contact")
    print("2.to view contacts")
    print("3.to search contact")
    print("4. to exit")

    choice=int(input("Enter your choice:"))

    if choice==1:
        name=str(input("Ente Name:"))
        phone=int(input("Enter Phone number:"))
        email=str(input("Enter Email:"))

        contact={"Name":name,"Phone":phone,"Email":email}
        contacts.append(contact)

    elif choice==2:
        for i in contacts:
            print(f"Name: {i['Name']}")
            print(f"Phone number: {i['Phone']}")
            print(f"Email: {i['Email']}")

    elif choice==3:
        search=str(input("Enter the name you want to search:"))
        for i in contacts:
            if i['Name']==search:
                print("Contact Found!")
                print(f"Name: {i['Name']}")
                print(f"Phone number: {i['Phone']}")
                print(f"Email: {i['Email']}")

    elif choice==4:
        print("bye")
        break

    else:
        print("Invalid input! please try again")
        continue
                












        















    





























