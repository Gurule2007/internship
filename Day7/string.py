def count(name):
    count = 0
    for i in name:
        if i=="A":
            count =count+1
            print (count)
        return count
n=input("Enter the Stering")   
count(n)