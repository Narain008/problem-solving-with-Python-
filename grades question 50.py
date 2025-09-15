# QUESTION----Write a Python program to calculate grade of a student based on marks.

a=int(input("Enter marks in english"))
b=int(input("Enter marks in hindi"))
c=int(input("Enter marks in maths"))
d=int(input("Enter marks in science"))
e=a+b+c+d
f=e/4
print(f)
if f>=90:
    print("A++")
elif f>=80:
    print("B++")
elif f>=70:
    print("C++")
elif f>=60:
    print("Fail")