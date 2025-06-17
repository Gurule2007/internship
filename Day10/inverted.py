dic={'a':1,'b':2,'c':1}
dic1={}
for key,value in dic.items():
    if value in dic1:
      dic1[value].append(key)
    else:
         dic1[value]=[key]

print(dic1)