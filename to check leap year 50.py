# QUESTION---Write a Python program to check whether a given year is a leap year.

a=int(input("Enter year"))
if a%4==0:
    print("Given year is leap year=",a)
else:
    print("Given year is not leap year")