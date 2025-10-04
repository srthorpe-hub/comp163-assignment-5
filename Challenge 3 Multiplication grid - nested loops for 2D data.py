
print("")
print("=== Challenge 3: Multiplication Table ===")
print("Multiplication Table:")
print(" ",end= "")
for column in range (1,11):
    print(f"{column:4}", end="")
    print()

for row in range(1,11):
    print(f"{row:2}",end=" ")
    for column in range(1,11):
        product = row * column
        print(f"{product:4}", end="")
    print()
#end of part 3