x = int(input("Enter number between 1 and 3"))

match x:
    case 1:
        print("one")

    case 2:
        print("two")
    case 3:
        print("three")
    case _:
        print("input is out of range")
