# count vowels

def CountVowel(word):
    count=0
    for i in word:
        if i in "aeiouAEIOU":
            count=count+1
    print(f"Number of vowels:{count}")

CountVowel("hi")


# list of number

def listOp(mylist):
    mylist.sort()
    print(f"smallest number:{mylist[0]}")
    print(f"largest number:{mylist[len(mylist)-1]}")

    mysum=0
    for i in mylist:
        mysum=mysum+i
    avg=mysum/len(mylist)

    print(f"average of numbers:{avg}")

listOp([1,2,3])


# student grade book

def std():
    records=[]
    average=[]
    while True:
        print("1.to add student name and marks")
        print("2.to view all students marks")
        print("3.to display the average marks of the class")
        print("4.search student by name and see marks")
        print("5.to exit")

        choice=int(input("Enter your choice:"))

        if choice==1:
            name=str(input("Enter the name:"))
            marks=float(input("Enter the marks"))
            std={"name":name,"marks":marks}
            records.append(std)
            average.append(marks)

        elif choice==2:
            for i in records:
                print(f"Student Name: {i['name']}")
                print(f"Student Marks:{i['marks']}")

        elif choice==3:
            for i in average:
                mysum=sum(average)
                avg=mysum/len(average)
            print(f"average marks of the class:{avg}")

        elif choice==4:
            search=str(input("Enter the name of student you want to search:"))
            for i in records:
                if i["name"]==search:
                    print("Student Found!")
                    print(f"student marks:{i['marks']}")

        elif choice==5:
            print("Exit Done")
            break

        else:
            print("Invalid Choice! please try again")
            continue
std()
                

        
    

    





















