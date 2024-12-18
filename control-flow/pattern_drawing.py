number = int(input("Enter the size of the pattern: "))
x = 0

while x < number:
    y = 0
    while y < number:
        print("*", end="")
        y += 1
    print()
    x += 1
