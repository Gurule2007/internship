try:
 num=int(input("Enter the number:-"))
 d=100/num
 f=input("Enter the file name:-")
 file=open(f,"w")

except ZeroDivisionError:
  print("can not zero")
except FileNotFoundError:
  print("File not found") 
else:
  print(f"Division is {d}")
  print(f"file open sucessfully") 
 