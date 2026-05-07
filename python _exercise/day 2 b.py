value1=int(input("Enter a number"))
value2=int(input("Enter another number"))

if (value1>value2):
    print(value1 , "is greater")

elif (value1<value2):
    print(value2 , "is greater")

else:
    print("none of them are greater")


C=int(input("Enter temperature in Celsius:"))
Fahrenheit= C * 9/5 + 32
print(Fahrenheit)

sub1=int(input("Enter marks1"))
sub2=int(input("Enter marks2"))
sub3=int(input("Enter marks3"))

average=(sub1+sub2+sub3)/3
print(average)



length=int(input("Enter length"))
width = int(input("Enter width"))

area = length * width
perimeter = 2 * (length + width)
print (area)
print(perimeter)

Salary = int(input("Enter your salary"))
print("your current Salary",Salary)
tax = Salary * 10 / 100

print(tax)
print("your net salary is" , Salary-tax)
