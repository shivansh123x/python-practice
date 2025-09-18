# program to count vowels and consosant

def countVC(mystr):
    vowel=0
    consonant=0
    for i in mystr:
        if i in "AEIOUaeiou":
            vowel=vowel+1
        else:
            consonant=consonant+1
    print("Number of vowels:",vowel)
    print("Number of consonant:",consonant)

countVC("hello")


# guessing game

import random
answer=random.randint(1,50)
attempt=0
while True:
        guess=int(input("Guess the output:"))
        attempt=attempt+1
        if guess==answer:
            print("correct!\n you played it well")
            print("total attempt:",attempt)
            break
            
        elif guess<answer:
            print("too low⬇")
        elif guess>answer:
            print("too high⬆")



#project 3 - simple expense tracker

items=[]
total_exp=[]
while True:
    print("1.to add items")
    print("2. view the items")
    print("3. total expenses")
    print("4.to exit")

    choice=int(input("Enter your choice please:"))

    if choice==1:
        product=str(input("Enter the product name:"))
        price=int(input("Enter the price :"))
        
        exp={"product":product ,"price": price}
        items.append(exp)

    elif choice==2:
        if not items:
            print("no items yet!")
        else:
            for i in items:
                print("product name:",i["product"])
                print("price:",i["price"])
    
    elif choice==3:
        total_exp= sum(i["price"] for i in items)
        print(f"total expense:{total_exp}")

    elif choice==4:
        print("goodbye")
        break

    else:
        print("Invalid choice:")
        break
    
            

















    
