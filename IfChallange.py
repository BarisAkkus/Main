name = input("What is your name ?")
age = int(input("Hi {0} . Please Enter Your Age ".format(name)))

if 18 <= age < 31 :
    print("Welcome {} , Have a nice holiday".format(name))
    
else:
    print("Sorry {} You do not meet the requirements ".format(name))
    

