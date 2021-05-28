import random


def get_integer(prompt):
    """
    Get an integer from Standart Input (stdin).append()
    The function will continue looping , and prompting
    the user, until a valid 'int' is entered.
    
    :param prompt: The String that the user will see, when they're prompted to enter the value    
    
    
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        #else:
        print("{} is not a valid number".format(temp))
            
        
highest = 1000
answer = random.randint(1,highest)
print(answer) # TODO: Remove after testing
guess = 0
print("Please guess number between 1 and {}: " .format(highest))

while guess!=answer :
    
    guess = get_integer(": ")
    if guess == 0 :
        break
    if guess == answer:
        print("Well done you guessed it true")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower") 