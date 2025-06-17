


number = float(input("Enter a number: "))

if number > 0:
    print("Number is positive")
    if number > 100:
        print("and greater than 100")
    else:
        print("and not greater than 100")
elif number < 0:
    print("Number is negative")
else:
    print("Number is zero")
