
s_num = 9

while True:

    guess = int(input("Guess the number: "))
    if s_num > guess:
        print("Too low")
    elif s_num < guess:
        print("Too high")
    else:
        print("Correct")
        break