try:
    num=int(input("Enter the number:-"))
    f=input("Enter the file name:-")
    file=open(f,"r")
    d=100/num
except FileNotFoundError:
    print("file not found")  
except ZeroDivisionError:
    print("can not divide zero")      