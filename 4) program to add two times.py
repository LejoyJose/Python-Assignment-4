h1=int(input("Hour:"))
m1=int(input("Minute:"))
s1=int(input("Second:"))

h2=int(input("Hour:"))
m2=int(input("Minute:"))
s2=int(input("Second:"))

hours=h1+h2+(m1+m2+(s1+s2)//60)//60
minutes=(m1+m2+(s1+s2)//60)%60
seconds=(s1+s2)%60

print(f"{hours}:{minutes}:{seconds}")
