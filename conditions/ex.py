
# 1) check the number is even or odd and if even then divisible by 8 or not also if odd then it is divisible by 5 or not 

a = int(input("enter the number"))
if a %2==0:
    print("even")
    if a%8==0:
        print("divisible by 8")
    else:
        print("not divisible by 8")
else:
    print("odd")
    if a%5==0:
        print("divisible by 5")
    else:
        print("not divisible by 5")



# 2) to find the second largest number among four numbers

a = int(input("enter first no"))
b = int(input("enter second no"))
c = int(input("enter third no"))
d = int(input("enter fourth no"))

if (a<b and a>c and a>d) or (a<c and a>b and a>d) or (a<d and a>b and a>c):
    print(a)
elif (b<a and b>c and b>d)or (b<c and b>a and b>d) or (b<d and b>a and b>c):
    print(b)
elif (c<a and c>b and c>d)or (c<b and c>a and c>d)or (c<d and c>a and c>b):
    print(c)
else:
    print(d)

# 2nd method

if a>b and a>c and a>d:     #a is largest
    if b>c and b>d :
        print(b)
    elif c>b and c>d :
        print(c)
    else:
        print(d)
elif b>a and b>c and b>d:     #b is largest
    if a>c and a>d :
        print(a)
    elif c>a and c>d :
        print(c)
    else:
        print(d)
elif c>b and c>a and c>d:     #c is largest
    if b>a and b>d :
        print(b)
    elif a>b and a>d :
        print(a)
    else:
        print(d)
else:                         #d is largest
    if b>a and b>c :
        print(b)
    elif a>b and a>c :
        print(a)
    else:
        print(c)



# 3) calculate taxi fare

distance = float(input("enter the distance"))
time = input("day or night")

if distance<=5:
    fare = 50
elif distance<=20:
    fare = 50 + (distance-5)*10
else:
    fare = 50+ 150 + (distance-20)*8

if time == "night":
    fare = fare + fare/4

new_fare = int(fare*100)/100
print(new_fare)    
# print(round(fare,2))   



# 4) triangle analyzer 

a = int(input("enter first side "))
b = int(input("enter second side"))
c = int(input("enter third side"))

if a + b > c and a + c > b and b + c > a:
    if a>=b and a>=c:
        largest, x, y = a, b, c
    elif b>=a and b>=c:
        largest, x, y =b, a, c
    else:
        largest, x, y = c, a, b
    
    if a==b==c:
        print("equilateral Acute")
    
    elif a==b or b==c or a==c:
        print("isosceles", end=" ")
        if x**2 + y**2 ==largest**2:
            print("right angled")
        elif x**2 + y**2 >largest**2:
            print("acute")
        else:
            print("obtuse")
    else:
        print("scalene", end = " ")
        if x**2 + y**2 ==largest**2:
            print("right angled")
        elif x**2 + y**2 >largest**2:
            print("acute")
        else:
            print("obtuse")
    
else: 
    print("invalid") 