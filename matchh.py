x=int(input("enter numeber:"))
match x:
    case 0:
         print("You entered zero")
    case 1:
        print("You entered one")
    case 2:
        print("You entered two")
    case 3:
        print("You entered three")
    case _:
        print("You entered a number other than one, two, or three")
