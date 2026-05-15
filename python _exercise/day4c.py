#if elif and else examples

age =int(input("enter your age"))
if age>18:
    print("you can watch the movies")
else:
    print("you can not watch the movies")


a=5
if a==3:
    print("yes")
else:
    print("no")

#find greater number

sum1=int(input("enter the sum"))
sum2=int(input("enter the sum2"))
sum3=int(input("enter the sum3"))

if sum1>sum2 and sum1>sum3:
    print("sum1 is greater")

elif sum2>sum3 and sum2>sum1:
    print("sum2 is greater")
elif sum3>sum1 and sum3>sum2:
    print("sum3 is greater")
else:
    print("invalid")

#max function to find greater number
max_num=max(sum1,sum2,sum3)
print(max_num)