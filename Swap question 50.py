# QUESTION 1---Write a Python program to swap two numbers without using a third variable.

a=int(input("Enter a no"))
b=int(input("Enter a no"))
print("Before swapping=",a,b)
a=a+b
b=a-b
a=a-b
print("After swapping=",a,b)