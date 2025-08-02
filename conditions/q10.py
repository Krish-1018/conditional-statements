# convert the time from 12 hour format to 24 hour format

hr = int(input("enter no of hours"))
min = int(input("enter no of minutes"))
sec = int(input("enter no of seconds"))
time = input("AM or PM ")

if time=="AM" and hr==12:
    print(F"00:{min}:{sec}AM")
elif hr==12 and time=="PM":
    print(F"{hr}:{min}:{sec}PM")
elif time=="AM":
    print(F"{hr}:{min}:{sec}AM")
elif time=="PM":
    print(F"{hr+12}:{min}:{sec}PM")    

