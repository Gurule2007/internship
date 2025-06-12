def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact *= i
    
    print(f"Factorial: {fact}")
    return fact

num = int(input("Enter the number:- "))

factorial(num)