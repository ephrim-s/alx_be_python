number = int(input("Enter a number to see its multiplication table: "))

for x in range(number):
    print("")
    for y in range(number):
        print("*", end="")
