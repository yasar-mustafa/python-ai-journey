# Functions

# def
# return
# parameter
# code modular writing

# functional thinking
# breaking code into parts

def calculate_total(hours_list):
    return sum(hours_list)


def calculate_average(hours_list):
    return sum(hours_list) / len(hours_list)


def performance_message(avg):
    if avg >= 4:
        return "Elite Level 🚀"
    elif avg >=2:
        return "Good Discipline 💪"
    else:
        return "Push Harder 🔥"

name = input("What is your name? ")
days = int(input("How many days of study data? "))

study_hours = []

for day in range(1, days + 1):
    hours = float(input(f"Hours studied on Day{day}:"))
    study_hours.append(hours)


total = calculate_total(study_hours)
average = calculate_average(study_hours)
message = performance_message(average)

print("\n--- Study Report ---")
print(f"Total Hours: {total}")
print(f"Average Hours: {average:.2f}")
print(message)