parrot = "Norwegian Blue"

print(parrot)

print("\nw \ne \nw \ni \nn\n")

print(parrot[3])
print(parrot[4])
print(parrot[3])
print(parrot[6])
print(parrot[8])
print()
print(parrot[-11])
print(parrot[-10])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])
print()
print(parrot[0:6])
print(parrot[3:5])

print(parrot[:9])

print(parrot[:6])
print(parrot[6:])
print(parrot[:])

#yeni

print(parrot[-4:-2])
print(parrot[-4:12])

print(parrot[0:6:2])
print(parrot[0:6:3])

#number = "9,223;372:036 854,775;807"
number = input("Please enter a series of numbers, using seperators you like : ")
#print(number[1::4]) #aynı

seperators = ""
for char in number:
    if not char.isnumeric():
        seperators = seperators + char

#number = "9,223;372:036 854,775;807"
#seperators = number[1::4]


#print(seperators)

values="".join(char if char not in seperators else " "for char in number).split()
print(sum([int(val)for val in values]))


quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""
# Use a for loop and an if statement to print just the capitals in the quote above.
for char in quote:
    if char.isupper():
        print(char)

