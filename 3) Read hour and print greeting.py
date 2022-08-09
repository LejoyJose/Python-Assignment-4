n=int(input("Enter time in hour"))
if(n>0 and n<12):
    print("Good Morning")
elif(n>=12 and n<18):
    print("Good Evening")
elif (n>=18 and n<24):
    print("Good Night")
else:
    print("please Enter a valid Hour")
