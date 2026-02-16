# day 4 numbers

name = input("Name :")
hours = float(input("How many hours do you study per day? "))
days = int(input("How many days will you keep this up? "))

total_hours = hours * days

print("\n--- Study Plan ---")
print(f"{name}, if you study {hours} hours/day for {days} days,")
print(f"you will complete {total_hours} total hours. 🚀")