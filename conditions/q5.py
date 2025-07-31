# Take a  number and check it is 1 digit number, or 2 digit number, or 3 digit number or something else.

a = int(input("enter the number"))

if a>=0 and a<10:
    print("one digit number")
elif a>=10 and a<100:
    print("two digit number")
elif a>=100 and a<1000:
    print("three digit number")        
