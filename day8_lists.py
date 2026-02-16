# Lists

# We will create a list.
# We will add data to the list.
# We will loop through the list.
# We will use max(), min(), and sum().

name = input("What is your name? ")
days = int(input("How many days of study data will you enter? "))

study_hours = []   # We create an empty list with the `study_hours` variable.

for day in range(1,days + 1):
    hours = float(input(f"Hours studied on day {day} :"))
    study_hours.append(hours)


print("\n--- Detailed Report ---")
print(f"Daily hours :{study_hours}")

total = sum(study_hours)  # We sum the values ​​in the list.

average = total / len(study_hours)  # We divide the total value in the list by the total number of items in the list.

print(f"Total Hours :{total}")
print(f"Average Hours :{average}")
print(f"Best Day :{max(study_hours)} Hours")
print(f"Lowest Day :{min(study_hours)} Hours")