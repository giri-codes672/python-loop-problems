# Find maximum number using for loop

numbers = [12, 45, 67, 23, 89, 34]

maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print("List:", numbers)
print("Maximum Number =", maximum)
