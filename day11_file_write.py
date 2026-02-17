# Day 11 – Writing to Files & Persistent Data  (Dosyaya Yazma & Kalıcı Veri)

def save_report(name, total, average):
    with open("study_report.txt","a", encoding="utf-8") as file:
        file.write(f"name :{name}\n")
        file.write(f"Total Hours :{total}\n")
        file.write(f"Average Hours :{average:.2f}\n")
        file.write("-"*15 + "\n")

name = input("What is your name? ")
days = int(input("How many days of study data? "))

study_hours = []

for day in range(1, days +1):
    hours = float(input(f"Hours studied on Day {day}"))
    study_hours.append(hours)

total = sum(study_hours)
average = total / len(study_hours)

print("\n--- Study Report ---")
print(f"Total Hours :{total}")
print(f"Average Hours :{average:.2f}")

save_report(name, total, average)

print("\nReport saved to study_report.txt ✅")