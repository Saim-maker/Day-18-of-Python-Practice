total = 0
for x in range(1,101):
    total = total + x
    print(x)


numbers = int(input("Enter a number: "))

even_numbers = 0
odd_numbers = 0

for x in range(1, numbers + 1):
    if x % 2 == 0:
        even_numbers = even_numbers + 1
    else:
        odd_numbers = odd_numbers + 1

print("Even numbers count:", even_numbers)
print("Odd numbers count:", odd_numbers)

n = int(input("Enter a number: "))
total = 0
for x in range(1, n + 1):
    if x%2 == 0:
        total = total + x
        print(total)