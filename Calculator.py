try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    print("What kind of operation do you want to perform?")
    print("Press + for addition")
    print("Press - for subtraction")
    print("Press / for division")
    print("Press * for multiplication")

    o = input("Enter operation: ")

    match o:
        case "+":
            print(f"The result is: {a + b}")
        case "-":
            print(f"The result is: {a - b}")
        case "/":
            print(f"The result is: {a / b}")
        case "*":
            print(f"The result is: {a * b}")
        case default:
            print("There was an error: invalid operation")

except Exception as e:
    print("Enter a valid value of a and b")
