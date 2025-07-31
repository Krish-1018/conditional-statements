#Take 3 integers A,B,C which denote the angles of a triangle, and return 'VALID'
#if the angles can form a valid triangle or 'NOT VALID' if the angles cannot form a valid triangle. 
#Print the type of triangle in case it is valid

a = int(input("enter first number"))
b = int(input("enter second number"))
c = int(input("enter third number"))

if a>0 and b>0 and c>0 and (a+b+c)==180:
  print("VALID")
  if a==b==c:
    print("EQUILATERAL")
  elif a==b or b==c or a==c:
    print("ISOSCELES")
  else:
    print("SCALENE")
else:
  print("NOT VALID")