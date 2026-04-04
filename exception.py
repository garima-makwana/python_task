try:
    number1=int(input("Enter Number:"))
    number2=int(input("Enter Another Number:"))
    result=number1/number2
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Please enter a valid number:")
else:
    print("Division successfull result is :",result)
finally:
    print("This block always runs.")