# try:
    # x = input("Enter first number: ")
    # y = int(input("Enter second number: "))
    # z = x + y  # int can not to plus to str
    # print(z)
# except TypeError:
    # print('can only concatenate str (not "int") to str')

try:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    z = x / y  # you cannot any numbers to divide with 0
except ZeroDivisionError as e:
    print(e)
    print("you cant any numbers to divide to zero")
except ValueError as e:
    print(e)
    print("you cannot divide any strings to any numbers")
except Exception as e:
    print(e)
    print("something went wrong")
else:
    print(z)
    print(f"{z:.2f}")
    print("All is well")
finally:
    if ZeroDivisionError or  ValueError or Exception == True:
        print("Try again!")
    else:
        print("Well done...")
    