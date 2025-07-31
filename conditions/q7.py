#Take a 4 digit integer denoting a year and print out "YES" if it is a leap year and "NO" if it is not a leap year.

a = int(input("enter a four digit number"))

if( a%4==0 and a%100!=0 ) or a%400==0:
  print("YES")
else:
  print("NO")