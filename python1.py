# This is a comment
# Post : Python Comment

# v = s/t
# v = ความเร็ว (m/s)
# s = ระยะทาง (m)
# t = ระยะเวลา (s)
print("Hello World 1")

"""
# v = s/t
# v = ความเร็ว (m/s)
# s = ระยะทาง (m)
# t = ระยะเวลา (s)
"""
print("Hello World 2")

"""
#
# Part; Python Variables
#
"""

x = 5
y = "Hey Bro"
print(x, y)

x = str(3)
y = int(3)
z = float(3)
print(type(x), type(y), type(z))

"""
#
# Part Variables name
#
"""

myvar = "John"
my_var = "John"
_my_var = "John" #ค่าtemp
myVar = "John" #ส่วนใหญ่นิยมใช้
MYVAR = "John"
MY_VAR = "John" #ค่าที่fixไม่ให้แก้ไข
myvar2 = "John"

# Camel Case
myVaribleName ="John"

#Pascal Case 
MyVaribleName ="John"

# snack Case
my_variable_name ="John"

"""
#
# Part : Python String
#
"""

x ="Hey Bro"
print (x)

y = """
1 Hey Bro 2 Hey Bro
3 Hey Boy
4 Hey Boy
5 Hey Boy """
print (y)

x = "Hey Boy"
print(x[2])
print(len(x))

print("Hey" in x)
print("what sup" not in x)
print(x.upper())
print(x.lower())
print(x.replace("Bro","Sis"))
print(x.split(" "))

a = "Apple"
b = "Banana"
print(a + " "+ b)
 
price = 20
word = f"price: {price:.2f}"
print(word)
