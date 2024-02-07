rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of clumns: "))
symbol = input("Enter your symbol: ")
print()

for x in range(rows):
    for y in range(columns):
        print(symbol, end=" ")
    print()

print()