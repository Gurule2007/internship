class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def is_even(number):
        return number % 2 == 0


print(Calculator.add(5, 3))  
print(Calculator.multiply(4, 6))  
print(Calculator.is_even(10))  
print(Calculator.is_even(11))  
