productCost=input("Enter Product cost")
sellPrice=input("Enter Selling cost")
if(sellPrice>productCost):
    print("Profit")
elif(sellPrice==productCost):
    print("No profit No loss")
else:
    print("Loss")
