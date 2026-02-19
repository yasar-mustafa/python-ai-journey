# Menu System (CLI App v1)
# Up until now, we've written to separate files. Today, the user will make a selection.

import csv

def add_record():
    name = input("Name :")
    days = int(input("How many days? :"))

    study_hours = []

    for day in range(1, days + 1):
        hours = float(input(f"Hours on Day {day} :"))
        study_hours.append(hours)

    total = sum(study_hours)
    average = total / len(study_hours)

    with open("study_hours.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([name, total, average])
    
    print("Record saved succesfully ✅")


def analyze_records():
    try:
        with open("study_hours.csv", "r", encoding="utf-8") as file:
            reader  = csv.reader(file)
            records = list(reader)

            if not records:
                print("No Data Found")
                return
            
            totals   = [float(row[1]) for row in records]
            averages = [float(row[2]) for row in records]

            print("\n--- Analysis ---")
            print(f"Total Records :{len(records)}")
            print(f"Best total hours :{max(totals)}")
            print(f"Min total hours :{min(totals)}")
            print(f"Highest average :{max(averages):.2f}")
            print(f"Lowest average :{min(averages):.2f}")


    except FileNotFoundError:
        print("No CSV file found !")




def main():
    while True:
        print("n\=== Study Tracker Menu ===")
        print("1 - Add new record")
        print("2 - Analyze records")
        print("3 - Exit")

        choice = input("Choose an option :")

        if choice == "1":
            add_record()
        elif choice == "2":
            analyze_records()
        elif choice == "3":
            print("Goodbye 🚀")
            break
        else:
            print("Invalid Option.")

if __name__ == "__main__":
    main()


# Today We Learned
    # Program Flow Control
    # while True
    # Function Organization
    # Simple CLI App Structure
    # name == "main"