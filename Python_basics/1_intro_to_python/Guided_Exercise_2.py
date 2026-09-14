print("\nSaving Calculator")
name = input("Whats your name?")
mon_saving = float(input("How much money do you save each month?"))
num_months = int(input("How many months do you want to keep saving?"))
total_saving = 0

for i in range(1, num_months + 1):
    total_saving += mon_saving
    print(f"Your month {i} your total of saves ir: {total_saving}")

print(f"\nYour total is: {total_saving}")
#