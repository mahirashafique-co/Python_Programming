#program of while loop
p = 0
while p < 5:
    print(p)
    p = p + 1

p = 0
while p < 5:
    p = p + 1
    print(p)

#program of if using break and pass
for i in range(0, 100):
    print(i)
    if (i == 50):
        break
print("end of program")

for i in range(8):

    if (i == 5):
        pass
    else:
        print(i)
print("end of program")


#program of find factorial
enter_Factorial = int(input("enter factorial"))

if enter_Factorial < 0:
    print("invalid input")

elif enter_Factorial == 0:
    print("factorial of 0 is 1")

else:
    fact = 1
    for i in range(1, enter_Factorial + 1): #start , step , skip
        fact = fact * i
    print(fact)


