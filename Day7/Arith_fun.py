def calculator(num1, num2, opera):
    if opera == "+":
        print(f"Addition: {num1+num2}")

    elif opera == "-":
        print(f"Subtraction: {num1-num2}")

    elif opera == "*":
        print(f"Multiplication: {num1*num2}")

    elif opera == "/":
        print(f"Division: {num1/num2}")

    elif opera == "**":
        print(f"Power: {num1**num2}")

    elif opera == "%":
        print(f"Modulus: {num1%num2}")

    else:
        print("Invalid input")

    
opera = input("Enter opeartor: ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
calculator(num1 , num2 , opera)



    
