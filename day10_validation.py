# Validation

# catching erroneous inputs (try/except)
# asking again (while loop)
# small refactoring

# "The program doesn't crash when the user types something nonsensical." This is a must-have in real-world software development.

def read_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please Enter a number (e.g., 7).")


def read_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a non-negative number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number (e.g., 2.5).")


def performance_message(avg):
    if avg >= 4:
        return "Elite Level"
    elif avg >= 2:
        return "Good Discipline"
    else:
        return "Push Harder"

name = input("What is your name? :")
days = read_int("How many days of study data? :")

study_hours = []

for day in range(1, days + 1):
    hours = read_float(f"Hours Studied on Day {day} :")
    study_hours.append(hours)


total = sum(study_hours)
average = total / len(study_hours)

print("\n--- Study Report ---")
print(f"Daily Hours   :{study_hours}")
print(f"Total Hours   :{total}")
print(f"Average Hours :{average:.2f}")
print("-"*15)
print(performance_message(average))