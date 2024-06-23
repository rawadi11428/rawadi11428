"""
#
# Part: Python Conditions
#
"""
i = 1
while i < 5:
    print("i = ", i)
    i+=1

i = 1
while i < 5:
    print("i = ", i)
    if i == 3:
        break
    i+=1
    
 # i = 1
# while i < 5:
#   print("i = ", i)
#   if i == 3:
#       break
#   i+=1

i = 1
while i < 5:
    print("i = ", i)
    i += 1
else :
    print("Game Over")


"""
#
# Part: Python For Loop
#
"""

fruits = ["Apple", "Banana", "Coconut"]
for x in fruits:
    print("Fruit:", fruits)

for x in fruits:
    print("Fruit:", fruits)
    if fruits == "Banana":
        break

for x in fruits:
    if fruits == "Banana":
        break
    print("Fruit:", fruits)
    
for x in fruits:
    if fruits == "Banana":
        continue
    print("Fruit:", fruits)

for x in range(len(fruits) + 1):
    print("Number =, x")

for x in range(5):
    print("Number = ", x)
else:
    print("Game Over")

adjs = ["Red", "Yellow", "Brown"]
fruits = ["Apple", "Banana", "Coconut"]
for adj in adjs:
    for fruit in fruits:
        print(adj, fruit) 