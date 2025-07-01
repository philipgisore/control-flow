#Define the height of the pyramid
rows = 5

#Outer loop to handle number of rows
i = 1
while i <= rows:
    #Print spaces first (for alignment)
    space = 1
    while space <= (rows - i):
        print(" ", end="")
        space += 1

    #Then print asterisks
    star = 1
    while star <= (2 * i - 1):
        print("*", end="")
        star += 1

    #Move to the next line
    print()
    i += 1
