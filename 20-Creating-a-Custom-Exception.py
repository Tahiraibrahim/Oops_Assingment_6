# Assingment-20

# Create a custom exception InvalidAgeError.
#  Write a function check_age(age) that raises this exception if age < 18.
#  Handle it with try...except.


class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise IndentationError("Age must be 18 or older.")
    else:
        print("Access granted.")

try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print("Custom Exception Caught:", e)
except ValueError:
    print("Please enter a valid number.")

