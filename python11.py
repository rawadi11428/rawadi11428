"""
#
# Part: Python Try Ezcept
#
"""
# The "try" block lets you test a block of code for errors.
# The "except" block lets you handle the errors.
# the "else" block lets you exectue code when there is no error.
# The "finally" block lets you execute code, regardless of the resulf of the try- and except block.

try:
    print(x)
    # do something ...
except NameError as e:
    print("Not defind! : ", e)
except:
    print("Something else went wrong!")

try:
    print("Hello World")
except:
    print("Something else went wrong!")
else:
    print("Nothing went wrong!")

try:
    print(x)
except:
     print("Something else went wrong!")
finally:
    print("Finished!")


# x = -1
# if x < 0:
#    raise Exception("Sorry, no number below zero.")

x = "Hello"
if not(x) is int:
    raise TypeError("only integers are allowed")
