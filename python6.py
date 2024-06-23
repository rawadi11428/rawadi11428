"""
#
# Part: Python Function
#
"""

def my_function():
    print("Hello World 3")
    print("Hello World 4")

my_function()
my_function()

# parameter
def my_name(fname):
    print("My name is ", fname)

my_name("Anya")

def my_name2(fname, Lname):
    print("My name is ", fname, Lname)

my_name2("Anya", "Roger")
my_name2(Lname = "Roger", fname = "Anya")

def my_name3(Lname = "Roger"):
    print("My last name is" , Lname)

my_name3()
my_name3("Paul")

def my_friuts(friuts):
    for friut in friuts:
        print(friut)

friuts = ["Apple", "Banana", "Coconut"]
my_friuts(friuts)


def red_potion(hp):
    return hp + 50
print("HP:", red_potion(100))
print("HP:", red_potion(70))