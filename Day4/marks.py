s1 = int(input("Enter the marks of subject 1:-"))
s2 = int(input("Enter the marks of subject 2:-"))
s3 = int(input("Enter the marks of subject 3:-"))
total=s1+s2+s3
pre=total/3

print("Total Marks:-",total)
print("precentage of marka:-",pre)

if pre<=100 and pre>=90:
    print("Grade A+")
elif pre<=90 and pre>=80:
    print("Grade A")
elif pre<=80 and pre>=60:
    print("Grade B")
elif pre<=60 and pre>=40:
    print("Grade c")
else:
    print("Fail")


