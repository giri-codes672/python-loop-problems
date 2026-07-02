# First 10 Fibonacci Numbers

a = 0
b = 1

print("First 10 Fibonacci Numbers:")

for i in range(10):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
