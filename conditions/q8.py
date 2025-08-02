#convert the time from 24 hour format to 12 hour format

hr = int(input("enter no of hours"))
min = int(input("enter no of minutes"))
sec = int(input("enter no of seconds"))

if hr==0:
    print(F"{12}:{min}:{sec}AM")
elif hr<12:
    print(F"{hr}:{min}:{sec}AM")
elif hr>12:
    print(F"{hr-12}:{min}:{sec}PM")
elif hr==12:
    print(F"{12}:{min}:{sec}PM")           
    