"""
#
# Part: Python JSON
# API = Application Programming Interface
#
"""

import json

#make a json (string)
x = '{"name": "John", "age": 20, "city": "Phuket"}'

# parse x
y = json.loads(x)

# Python Dictionry
print(y)
print(y["city"])

# Python Dictionry
a = {
    "name": "John",
    "age": 20,
    "city": "Phuket"
}

# convert into JSON (String)
b = json.dumps(a)

# JSON String
print(b)
