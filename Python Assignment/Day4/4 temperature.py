


temperature = float(input("Enter the temperature: "))

if temperature > 35:
    print("Too Hot")
elif temperature >= 25 and temperature <= 35:
    print("Normal Weather")
elif temperature >= 15 and temperature < 25:
    print("Cool")
else:
    print("Too Cold")
