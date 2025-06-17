dic={"apple":10,"banana":5}
try:
    fruit=input("Enter a fruit name:-")
    price=dic[fruit]
    file=input("Enter the file name:-")
    with open(file,"r") as file:
        content=file.read()
        print(f"the price:{price}")
        print(f"the file content:{content}")
except(KeyError,FileNotFoundError) as e:
    print("file not found")
    print(e)       