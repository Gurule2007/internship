data=[10,20,30,"Aditya"]
try:
    ind=int(input("Enter The index:-"))
    val=data[ind]
    f=float(val)
   
except(IndexError,ValueError) as e:
    print(e)