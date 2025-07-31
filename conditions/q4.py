# Take three number and print the biggest number 

a = int(input("enter first number"))
b = int(input("enter second number"))
c = int(input("enter third number"))

if a>b and a>c:
    print(a,"is biggest")
elif b>a and b>c:
    print(b,"is biggest")
elif c>a  and c>b:
    print(c,"is biggest")        
