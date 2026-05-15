#match case simple program

browser = str(input("enter your browser\n"))
browser = browser.lower()
match browser:
    case"chrome":
        print("browser is chrome")
    case"firefox":
        print("browser is firefox")
    case _:
        print("no browser found")

year=int(input("enter your year"))



