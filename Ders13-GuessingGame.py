answer = 5
print("Please guess number between 1 and 10: ")
guess = int(input())


if guess!=answer :
    if guess < answer:
        print("Please guess higher")
    else: 
        print("please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done you guessed it true")
    else:
        print("Sorry you guessed it wroong")
else:
    print("You got it first time")


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



