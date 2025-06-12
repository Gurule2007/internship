print("Shooping Bill")
  
item_name  = input("Enter the Itam name :-")
Quantity = int(input("Enter the Quality :-"))
price = int(input("Enter the price :-"))
Total = Quantity*price
discount= Total *0.1
total =Total-(discount*0.1)
gst =total *0.18
total=gst+total 
print("\nShooping Bill")
print("Enter the Item:-",item_name)
print("Enter the Quantity:-",Quantity)
print("Enter the Price:-",price)
print("Enter the Calculation:-",Total)
print("Enter the discount",discount)
print("GST",gst)
print("Total amo",total)

