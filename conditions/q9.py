#take three angles and check if the triangle is isosceles or not

a = int(input("enter first angle "))
b = int(input("enter second angle"))
c = int(input("enter third angle"))

if (a==b)and a!=c:
    print("isosceles")
elif (b==c)and b!=a:
    print("isosceles") 
elif (a==c)and a!=b:
    print("isosceles")
else:
    print("not isosceles")   

    