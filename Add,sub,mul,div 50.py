# QUESTION 4-----Write a Python program to accept two integers and perform addition, subtraction, multiplication, division, and modulus.

a=int(input("Enter 1 no for addition"))
b=int(input("Enter 2 no for addition"))
c=a+b
print("Adittion of 2 number is=",c)

d=int(input("Enter 1 no for subtraction"))
e=int(input("Enter 2 no for subtraction"))
f=d-e
print("Subtraction of 2 no is=",f)

g=int(input("Enter 1 no for multiplication"))
h=int(input("Enter 2 no for multiplication"))
i=g*h
print("Multiplication of 2 no is=",i)

j=int(input("Enter 1 no for division"))
k=int(input("Enter 2 no for division"))
l=j/k
print("Division of 2 no is=",l)

m=int(input("Enter 1 no for division"))
n=int(input("Enter 1 no for division"))
o=m/n
if n==0:
    print("error cannot divide by zero")
else:
    print("Remainder is=",o)