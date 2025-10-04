
print("=== Challenge 2: Prime Number Checker ===")
new_number = int(input("Enter a number: "))
print(f"Testing divisors from 2 to {new_number - 1}...")
for i in range(2, (new_number - 1)) :
    if new_number % i == 0:
        new_number / 2
        print(f"{new_number} is not prime (divisible by 3)")
        break
else:
    print(f"{new_number} is prime!")

#end of part 2