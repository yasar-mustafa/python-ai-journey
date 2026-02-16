# Study tracker

name = input("what is your name? ")
days = int(input("How many days will you study? "))

total_hours = 0

for day in range(1,days + 1):
    hours = float(input(f"How many hours did you study on Day {day}? "))
    total_hours += hours

print("\n--- Study Summary ---")
print(f"{name}, you studied {total_hours} hours in total.")

average = total_hours / days

print(f"Your Daily average is {average:.2f} hours.")   # `float` specifies how many decimal places a number should have. `2f - 3f ....`

if average >= 4:
    print("Elite Consistency 🚀")
elif average >= 2:
    print("Good Discipline 💪")
else:
    print("You can push harder 🔥")