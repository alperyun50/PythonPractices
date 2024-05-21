# creating a custom exception
class JustNotCoolError(Exception):
    pass

x = 2

try:
    #print(x/1)
    # if not type(x) is str:
    #     raise TypeError("Only strings are allowed!")
    # raise Exception("Im a custom exception!")
    raise JustNotCoolError("this is just not cool, man!")
except NameError:
    print("Something is probably undefined!")
except ZeroDivisionError:
    print("You can't divide by 0!")
except Exception as error:
    print(error)
else:
    print("No errors!")
finally:
    print("I always run!")