# Question-- Write a Python program to find the largest of three numbers.

a=float(input("Enter 1 no"))
b=float(input("Enter 2 no"))
c=float(input("Enter 3 no"))
if a>=b and a>=c:
    print("Largest no is=",a)
elif b>=c and b>=a:
    print("Largest no is=",b)
else:
    print("Largest no is=",c)