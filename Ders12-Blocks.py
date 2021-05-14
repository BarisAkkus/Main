name = input("Please enter your name: ")
age = int(input("How old are you, {0}".format(name)))
print(age)

#if age >=18:
#    print("You can vote")
#    print("Please put an X in the b0x")
#else:
#    print("Please come back in {0} years".format(18-age))
#elif age ==900:
#    print("Sorry , Yoda, you die in Return of the")

if age <18:
    print("Hi {1} Please come back in {0} years".format(18-age,name))
elif age ==900:
    print("Sorry , Yoda, you die in Return of the")
else:
    print("You can vote")
    print("Please put an X in the b0x")

