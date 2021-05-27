import random


def get_integer(prompt):
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
    # guess = int(input())
    # if guess == answer:
    #     print("Well done you guessed it true")
    # else:
    #     print("Sorry you guessed it wroong")



# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer :
#         print("Well done, you guessed it right")
#     else:
#         print("Sorry you have guessed it wrong")
# elif guess > answer:
#     print("Please guess lower")
#     guess=int(input())
#     if guess == answer:
#         print("Well done , you guessed it right")
#     else:
#         print("Sorry you have guessed it wrong")
# else:
#     print("You got it first time")

#comment kaldırmak için ctrl k c ve ctrl k u



