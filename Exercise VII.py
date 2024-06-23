def check_odd_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

odd_numbers = []
even_numbers = []

for i in range(1, 21):
    result = check_odd_even(i)
    if result == "Even":
        even_numbers.append(i)
    else:
        odd_numbers.append(i)

print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)
    