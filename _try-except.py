try:
    numerator=int(input("enter numerator:"))
    denominator=int(input("enter denominator:"))
    result=numerator/denominator
    print(f"result is {result}")
except ZeroDivisionError:
    print("numerator cannot be divided by zero")
except ValueError:
    print("enter valid integer")
