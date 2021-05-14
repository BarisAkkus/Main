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

number = "9,223;372:036 854,775;807"
print(number[1::4])

number = "9,223;372:036 854,775;807"
seperators = number[1::4]
print(seperators)

values="".join(char if char not in seperators else " "for char in number).split()
print([int(val)for val in values])


