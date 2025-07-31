#take a number and check if it is integer or decimal number

n = float(input("enter the number"))

integer_prt = int(n)#if n=integer_prt then it is integer
decimal_prt = n - integer_prt

if decimal_prt==0:
    print("number is integer")
else:
    print("number is decimal")    