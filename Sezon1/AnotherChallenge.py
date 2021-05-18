print("Please choose your option from the list below :" 
      "\n1. Learn Python\n2. Learn Java\n3. Go swimming\n4. Have dinner "
      "\n5. Go to bed\n0. Exit")


while True:
    giris = int(input("What to do"))
    if giris == 1:
        print("You choose the Learn Python")
    elif giris == 2:
        print("You must Learn Java")
    elif giris == 3:
        print("You must Go to swimming")
    elif giris == 4:
        print("Have dinner")
    elif giris == 5:
        print("Go to bed")
    elif giris == 0:
        break
    else:
        print("\nPlease choose your option from the list below :" 
              "\n1. Learn Python\n2. Learn Java\n3. Go swimming\n4. Have dinner "
              "\n5. Go to bed\n0. Exit")

#while True:
    # choice=input()
    
    # if choice == "0":
    #     break
    # elif choice in "12345":
    #     print("You chose {}".format(choice))
        