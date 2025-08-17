# check if a three digit number is palindrome or not

a = int(input(" enter the number"))
first = a//100
last = a%10

if first ==last:
    print("palindrome number")
else:
    print("not palindrome number")

#2nd method

first=a//100
last = a%10
middle = (a//10)%10
rev = first*100 + middle*10 + last
if a ==rev:
    print("palindrome number")
else:
    print("not palindrome number")

