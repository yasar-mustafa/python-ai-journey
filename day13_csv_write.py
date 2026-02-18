# CSV Logic (Transition to Real Data Format)
# We are now switching from .txt to a more professional format: CSV.
# This is fundamental to data science.

# What we learned:
        # import csv
        # csv.writer
        # actual data format
        # saving data row by row

import csv

def save_to_cvs(name, total, average):
    with open("study_hours.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([f"Name :{name}, Total :{total}, Avg. :{average}"])


name = input("What is your name? :")
days = int(input("How many days of study data? :"))

study_hours = []

for day in range(1, days + 1):
    hours = float(input(f"Hours studied on Day {day} :"))
    study_hours.append(hours)

total   = sum(study_hours)
average = total / len(study_hours)

print("\n--- Study Report ---")
print(f"Total hours: {total}")
print(f"Average hours: {average:.2f}")


save_to_cvs(name, total, average)

print("\nData Saved to study_data.csv ✅")