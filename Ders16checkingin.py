parrot = "norwegian blue"

letter = input("Enter a character : ")

if letter.casefold() in parrot:
    print("{} is in {}".format(letter,parrot))
    
else:
    print("I dont need that letter")



