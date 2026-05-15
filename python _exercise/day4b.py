#program of find leap year

year = int(input("enter the year"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap year")      # 2000
        else:
            print("not leap year")  # 1900
    else:
        print("leap year")          # 2024
else:
    print("not leap year")          # 2023

