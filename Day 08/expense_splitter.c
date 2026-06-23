people = int(input("Enter number of people: "))
total = 0

for i in range(people):
    amount = float(input(f"Enter expense of person {i+1}: "))
    total += amount

share = total / people

print("\nTotal Expense:", total)
print("Each person should pay:", round(share, 2))


