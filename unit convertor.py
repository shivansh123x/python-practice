# unit convertor

def convertor():
    while True:
        print("1. kilometer ↔ miles")
        print("2. kilogram ↔ pounds")
        print("3. celsius ↔ fahrenhiet")
        print("4. exit")

        choice=int(input("Enter your choice:"))

        if choice==1:
            def distance():
                while True:
                    print("1. kilometer to miles")
                    print("2. miles to kilometer")
                    print("3. exit")

                    ch=int(input("Select your choice:"))

                    if ch==1:
                        kilometer=int(input("Enter the distance in kilometers:"))
                        miles=kilometer/1.6
                        print("Distance in miles:", miles)

                    elif ch==2:
                        miles=int(input("Enter the distance in miles:"))
                        kilometer=miles*1.6
                        print("Distance in kilometers:",kilometer)

                    elif ch==3:
                        print("bye")
                        break

                    else:
                        print("Invalid choice! please try again")
                        continue

            distance()
            


        elif choice==2:
            def weight():
                while True:
                    print("1. kilogram to pounds")
                    print("2. pounds to kilogram")
                    print("3. exit")

                    ch=int(input("Select your choice:"))

                    if ch==1:
                        kg=float(input("Enter the wieght in kilogram:"))
                        pound=kg*2.2
                        print("Wieght in pounds:",pound)

                    elif ch==2:
                        pound=float(input("Enter wieght in pounds:"))
                        kg=pound/2.2
                        print("Wieght in kilogram:",kg)

                    elif ch==3:
                        print("bye")
                        break

                    else:
                        print("Invalid choice! please try again")
                        continue

            weight()

        elif choice==3:
            def temperature():
                while True:
                    print("1.celcius to fahrenhiet")
                    print("2.fahrenhiet to celsius")
                    print("3. exit")

                    ch=int(input("Select your choice:"))

                    if ch==1:
                        cel=float(input("Enter temperature in celsius:"))
                        fah=(cel*9/5)+32
                        print("Temperature in fahrenhiet:",fah)
    
                    elif ch==2:
                        fah=float(input("Enter temperature in fahreniet:"))
                        cel=(fah-32)*5/9
                        print("Temperature in celsius:",cel)

                    elif ch==3:
                        print("bye")
                        break
    
                    else:
                        print("Invalid choice! please try again")
                        continue
            temperature()

        elif choice==4:
            print("Bye")
            break

        else:
            print("Invalid choice! please try again")
            continue

convertor()
















                
