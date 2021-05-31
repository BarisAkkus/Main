def fizz_buzz(number:int) -> int:
    if number % 15 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz "
    elif number %5 == 0:
        return "buzz"
    else:
        return (number)
for i in range(101):
    print(fizz_buzz(i))