#List

r = int(input("Enter row: "))
c = int(input("Enter col: "))

arr = []

for i in range(r):
    print(f"Row {i+1}")
    row = []
    for j in range(c):
        n = float(input(f"Enter number{j+1}: "))
        row.append(n)
    arr.append(row)

x = float(input("\nSearch: "))

print("\nThe numbers are:")
for row in arr:
    for val in row:
        print(val, end=" ")
    print()  

pos = []
for i in range(r):
    for j in range(c):
        if arr[i][j] == x:
            pos.append(f"Row {i}, Col {arr[i][j]}")

if pos:
    print(f"\nNumber {x} found at " + " and ".join(pos))
else:
    print(f"\nNumber {x} not found.")
