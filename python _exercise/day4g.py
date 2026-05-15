# print triangle

for i in range(0,6):
    print("*" * i)

print(" ")

#print reverse triangle

for i in range(6,0,-1):
    print("*" * i)

print(" ")

#print paramid

for i in range(0,6):
    print(" "* (5-i)+"*"*(2*i-1))