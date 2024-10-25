rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the numer of columns: "))
symbol = input ("Enter a symbol: ")

for x in range (rows):
    for y in range (columns):
        print (symbol, end=" ")
    print()