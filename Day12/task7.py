lock=False
try:
    lock=True
    print("lock")

    result=1/0
    print("Result",result) 

except Exception as e:
    print(e)

finally:
    lock=False
    print("lock released")