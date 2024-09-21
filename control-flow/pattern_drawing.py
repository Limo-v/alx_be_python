size = int(input("Enter the size of the pattern:"))

row = 1
while row <= size:
    for elem in range(0, size):
        print("*", end="")
    print("\n")
    row += 1